#!/usr/bin/env python3
"""
inventario.py — Etapa 1 do plano: inventariar skills e agentes instalados.

Varre ~/.claude/skills/*/SKILL.md e ~/.claude/agents/*.md e escreve, no bundle
OKF em wiki/:

  wiki/skills/<nome>.md     1 conceito por skill  (type: Skill)
  wiki/agentes/<nome>.md    1 conceito por agente (type: Agente)
  wiki/clusters/<id>.md     grupos de skills que disputam a mesma intenção (type: Cluster)
  wiki/*/index.md           listagens
  wiki/index.md             listagem raiz
  wiki/log.md               linha de registro

Preserva, em páginas já existentes, o frontmatter `migracao:` e a seção
`## Notas de migração`. Todo o resto é regenerado.

Uso: python3 tools/inventario.py [--skills DIR] [--agents DIR] [--wiki DIR] [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

import yaml

VERSION = "1.0.0"
ATOR = f"inventario.py/{VERSION}"
HOME = Path.home()
RAIZ = Path(__file__).resolve().parent.parent
ESTAGIOS = [
    "inventariado", "mapeado", "skill", "tools", "contrato",
    "loop", "testado", "aprovado", "descontinuado",
]

# ---------------------------------------------------------------------------
# Clusters: regras explícitas (nome/prefixo ou palavras na descrição).
# Ordem importa: a primeira regra que casar vence.
# ---------------------------------------------------------------------------
CLUSTERS: list[dict] = [
    {"id": "reels", "titulo": "Reels / vídeo curto vertical",
     "nomes": ["reel-edita-inema", "reel-edita-inematds", "forja-reel", "roteirista-inema", "talking-head-recut"],
     "palavras": ["reel", "reels", "short", "shorts", "tiktok", "9:16", "vertical"]},
    {"id": "video-explicativo", "titulo": "Vídeo explicativo / narrado",
     "nomes": ["video-explicativo", "videoprodutor", "faceless-explainer", "video-demonstrativo", "product-launch-video", "pr-to-video"],
     "palavras": ["explicativo", "explainer", "narrad"]},
    {"id": "curso", "titulo": "Curso HTML (trilhas/módulos)",
     "nomes": ["formato-curso", "formato-curso-v2", "formato-curso-v3", "formato-curso-v4", "formato-curso-v5", "revisar-curso", "videos-cursos-inema", "course-completer"],
     "palavras": ["curso", "trilha", "módulo", "modulo"]},
    {"id": "avatar", "titulo": "Avatar falante (HeyGen)",
     "nomes": ["avatar-heygen-nei", "heygen-cli", "heygen-mcp", "heygen-video-nei", "dublagem-compasso"],
     "palavras": ["avatar", "heygen", "dublagem"]},
    {"id": "hyperframes", "titulo": "HyperFrames (motor HTML→MP4)",
     "prefixos": ["hyperframes"],
     "nomes": ["general-video", "motion-graphics", "music-to-video", "slideshow", "embedded-captions", "remotion", "remotion-best-practices", "remotion-to-hyperframes", "scroll-film-studio"],
     "palavras": ["hyperframes"]},
    {"id": "pixflow", "titulo": "Pixflow (imagens → filme sem IA de vídeo)",
     "prefixos": ["pixflow"], "nomes": ["diretor-animacao", "videoanima", "filme"], "palavras": ["pixflow", "parallax"]},
    {"id": "video-ia", "titulo": "Vídeo por IA generativa (Seedance/Kling/Veo)",
     "nomes": ["video-ia", "kling-3-0", "seedance-loop-prompt", "ugc-seedance25", "mestre-direcao-dinamica", "video-plan-editor", "auditor-video-ia", "3d-animation-creator", "animation-designer"],
     "palavras": ["seedance", "kling", "veo", "gerador de vídeo", "vídeo por ia"]},
    {"id": "comfy", "titulo": "ComfyUI", "prefixos": ["comfy"], "palavras": ["comfyui", "comfy"]},
    {"id": "inemaref", "titulo": "Séries / HQ / referências de personagem",
     "prefixos": ["inemaref"], "palavras": ["quadrinho", "manga", "série", "serie", "hq"]},
    {"id": "imagens", "titulo": "Geração/edição de imagens",
     "nomes": ["imagens-agnes", "videos-agnes", "capa-inema", "generate", "algorithmic-art", "design-dna", "theme-factory", "brand-guidelines"],
     "palavras": ["imagem", "imagens", "flux", "magnific"]},
    {"id": "printing-press", "titulo": "Printing Press (CLI a partir de API)", "prefixos": ["printing-press"]},
    {"id": "making-of", "titulo": "Making-of / simulações", "prefixos": ["making-of"]},
    {"id": "conselho", "titulo": "Conselho de Agentes / análise estruturada",
     "nomes": ["fs-seis-chapeus", "grill-me", "os-coach", "maestro-roteador", "fable-mindset", "memory-audit", "session-handoff", "session-statusline"],
     "palavras": ["conselho", "chapéus", "seis chapeus"]},
    {"id": "pesquisa-web", "titulo": "Pesquisa / navegação / extração web",
     "nomes": ["agent-browser", "agent-reach", "espiona-ads", "pp-skool", "website-intelligence", "clima", "watch"],
     "palavras": ["pesquisa", "navegador", "browser", "scrap", "skool"]},
    {"id": "publicacao", "titulo": "Publicação / portal / landing",
     "nomes": ["atualiza-portal", "projetos-landing-guia", "web-artifacts-builder", "anuncio-edita", "audit-ablacao", "property-360"],
     "palavras": ["portal", "landing", "github pages"]},
    {"id": "dev-tooling", "titulo": "Ferramentas de desenvolvimento / skills / MCP",
     "nomes": ["skill-creator", "polyskill", "mcp-builder", "avaliar-erros-de-fluxos", "doc-coauthoring", "excalidraw-diagram-generator", "beautiful-mermaid", "figma", "impeccable", "media-use", "silver-platter", "roteiro"],
     "palavras": ["skill", "mcp", "n8n", "diagrama"]},
]


# ---------------------------------------------------------------------------
# util
# ---------------------------------------------------------------------------
def agora() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def hoje() -> str:
    return dt.date.today().isoformat()


def split_frontmatter(texto: str) -> tuple[dict, str]:
    """Retorna (frontmatter_dict, corpo). Frontmatter ausente → ({}, texto)."""
    if not texto.startswith("---"):
        return {}, texto
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", texto, re.S)
    if not m:
        return {}, texto
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, texto[m.end():]


def dump_frontmatter(fm: dict) -> str:
    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=200).rstrip() + "\n---\n"


def secao(corpo: str, titulo: str) -> str:
    """Extrai o conteúdo de uma seção '## titulo' (sem o cabeçalho)."""
    m = re.search(rf"^## {re.escape(titulo)}\s*\n(.*?)(?=^## |\Z)", corpo, re.S | re.M)
    return m.group(1).strip() if m else ""


def uma_linha(s: str, n: int = 220) -> str:
    s = re.sub(r"\s+", " ", (s or "")).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def yaml_str(s):
    return "" if s is None else str(s)


# ---------------------------------------------------------------------------
# leitura de skills / agentes
# ---------------------------------------------------------------------------
def ler_skill(dir_skill: Path) -> dict | None:
    skill_md = dir_skill / "SKILL.md"
    if not skill_md.exists():
        return None
    texto = skill_md.read_text(encoding="utf-8", errors="replace")
    fm, corpo = split_frontmatter(texto)
    nome = str(fm.get("name") or dir_skill.name)
    desc = yaml_str(fm.get("description"))
    # gatilhos: frases entre aspas na descrição
    gatilhos = re.findall(r"[\"“]([^\"”]{3,60})[\"”]", desc)
    # arquivos e subpastas
    subpastas = sorted(p.name for p in dir_skill.iterdir() if p.is_dir() and not p.name.startswith("."))
    n_arquivos = sum(1 for _ in dir_skill.rglob("*") if _.is_file())
    scripts = sorted(str(p.relative_to(dir_skill)) for p in dir_skill.rglob("*")
                     if p.is_file() and p.suffix in {".py", ".sh", ".mjs", ".js", ".ts"} and "node_modules" not in p.parts)
    # ferramentas citadas no corpo (heurística)
    corpo_l = corpo.lower()
    ferramentas = sorted({t for t in [
        "ffmpeg", "whisper", "groq", "hyperframes", "remotion", "comfyui", "pixflow", "heygen", "magnific",
        "yt-dlp", "inemavox", "tts", "chatterbox", "flux", "kling", "seedance", "veo", "playwright",
        "agent-browser", "supabase", "vercel", "github", "python", "node", "mcp", "telegram", "openai", "gemini",
    ] if t in corpo_l})
    # cabeçalhos do SKILL.md = mapa do processo
    cabecalhos = [h.strip() for h in re.findall(r"^#{1,3}\s+(.+)$", corpo, re.M)][:25]
    return {
        "nome": nome,
        "pasta": dir_skill.name,
        "path": str(skill_md),
        "descricao": desc,
        "versao": yaml_str(fm.get("version")),
        "invocacao_modelo": not bool(fm.get("disable-model-invocation")),
        "gatilhos": gatilhos[:12],
        "subpastas": subpastas,
        "n_arquivos": n_arquivos,
        "scripts": scripts[:30],
        "ferramentas": ferramentas,
        "cabecalhos": cabecalhos,
        "tamanho_skill_md": len(texto),
        "mtime": dt.date.fromtimestamp(skill_md.stat().st_mtime).isoformat(),
    }


def ler_agente(arq: Path) -> dict:
    texto = arq.read_text(encoding="utf-8", errors="replace")
    fm, corpo = split_frontmatter(texto)
    return {
        "nome": str(fm.get("name") or arq.stem),
        "path": str(arq),
        "descricao": yaml_str(fm.get("description")),
        "modelo": yaml_str(fm.get("model")),
        "tools": fm.get("tools") if isinstance(fm.get("tools"), (list, str)) else "",
        "cabecalhos": [h.strip() for h in re.findall(r"^#{1,3}\s+(.+)$", corpo, re.M)][:20],
        "tamanho": len(texto),
        "mtime": dt.date.fromtimestamp(arq.stat().st_mtime).isoformat(),
    }


# ---------------------------------------------------------------------------
# clusters
# ---------------------------------------------------------------------------
def cluster_de(skill: dict) -> str:
    nome = skill["pasta"]
    desc = (skill["descricao"] or "").lower()
    for c in CLUSTERS:
        if nome in c.get("nomes", []):
            return c["id"]
        if any(nome.startswith(p) for p in c.get("prefixos", [])):
            return c["id"]
    for c in CLUSTERS:
        if any(p in desc for p in c.get("palavras", [])):
            return c["id"]
    return "outros"


# ---------------------------------------------------------------------------
# escrita das páginas (preservando migracao + notas)
# ---------------------------------------------------------------------------
def carregar_existente(arq: Path) -> tuple[dict, str]:
    if not arq.exists():
        return {}, ""
    fm, corpo = split_frontmatter(arq.read_text(encoding="utf-8", errors="replace"))
    return fm, secao(corpo, "Notas de migração")


def pagina_skill(s: dict, cluster: str, existente_fm: dict, notas: str) -> str:
    mig = existente_fm.get("migracao") if isinstance(existente_fm.get("migracao"), dict) else {}
    mig = {
        "estagio": mig.get("estagio") or "inventariado",
        "cluster": mig.get("cluster") or cluster,
        "destino": mig.get("destino") or "",
        "notas": mig.get("notas") or "",
        "atualizado": mig.get("atualizado") or hoje(),
    }
    fm = {
        "type": "Skill",
        "title": s["nome"],
        "description": uma_linha(s["descricao"]),
        "resource": f"file://{s['path']}",
        "tags": ["skill", mig["cluster"]],
        "sources": [{"path": s["path"], "author": "human:nei", "last_modified": s["mtime"]}],
        "generated": {"by": ATOR, "at": agora()},
        "status": "draft",
        "related": [f"clusters/{mig['cluster']}"],
        "skill": {
            "versao": s["versao"],
            "invocacao_pelo_modelo": s["invocacao_modelo"],
            "arquivos": s["n_arquivos"],
            "subpastas": s["subpastas"],
            "scripts": s["scripts"],
            "ferramentas": s["ferramentas"],
            "gatilhos": s["gatilhos"],
            "tamanho_skill_md": s["tamanho_skill_md"],
        },
        "migracao": mig,
    }
    if existente_fm.get("verified"):
        fm["verified"] = existente_fm["verified"]
    linhas = [dump_frontmatter(fm), f"# {s['nome']}\n"]
    linhas.append("## Descrição (do SKILL.md)\n")
    linhas.append((s["descricao"] or "_sem descrição_") + "\n")
    linhas.append("## Mapa (etapa 1 do plano)\n")
    linhas.append("| Campo | Valor |\n|---|---|")
    linhas.append(f"| Tarefa | {uma_linha(s['descricao'], 160) or '—'} |")
    linhas.append(f"| Entradas (gatilhos) | {', '.join(s['gatilhos']) or '— (extrair manualmente)'} |")
    linhas.append(f"| Ferramentas citadas | {', '.join(s['ferramentas']) or '—'} |")
    linhas.append(f"| Processo (cabeçalhos) | {' → '.join(s['cabecalhos'][:10]) or '—'} |")
    linhas.append("| Saída | _preencher no mapeamento_ |")
    linhas.append("| Validação | _preencher no mapeamento_ |")
    linhas.append(f"| Progressive disclosure | subpastas: {', '.join(s['subpastas']) or 'nenhuma'} · SKILL.md com {s['tamanho_skill_md']:,} chars |\n")
    if s["scripts"]:
        linhas.append("## Scripts (candidatos a `agent/tools/`)\n")
        linhas.extend(f"- `{x}`" for x in s["scripts"])
        linhas.append("")
    linhas.append(f"## Cluster\n\n[{mig['cluster']}](../clusters/{mig['cluster']}.md)\n")
    linhas.append("## Notas de migração\n")
    linhas.append((notas or "_(vazio — a interface e o agente escrevem aqui)_") + "\n")
    return "\n".join(linhas)


def pagina_agente(a: dict, existente_fm: dict, notas: str) -> str:
    mig = existente_fm.get("migracao") if isinstance(existente_fm.get("migracao"), dict) else {}
    mig = {
        "estagio": mig.get("estagio") or "inventariado",
        "cluster": mig.get("cluster") or "conselho",
        "destino": mig.get("destino") or "",
        "notas": mig.get("notas") or "",
        "atualizado": mig.get("atualizado") or hoje(),
    }
    fm = {
        "type": "Agente",
        "title": a["nome"],
        "description": uma_linha(a["descricao"]),
        "resource": f"file://{a['path']}",
        "tags": ["agente", "subagente"],
        "sources": [{"path": a["path"], "author": "human:nei", "last_modified": a["mtime"]}],
        "generated": {"by": ATOR, "at": agora()},
        "status": "draft",
        "agente": {"modelo": a["modelo"], "tools": a["tools"], "tamanho": a["tamanho"]},
        "migracao": mig,
    }
    linhas = [dump_frontmatter(fm), f"# {a['nome']}\n", "## Descrição\n", (a["descricao"] or "_sem descrição_") + "\n"]
    linhas.append("## Mapa\n\n| Campo | Valor |\n|---|---|")
    linhas.append(f"| Modelo | {a['modelo'] or 'herdado'} |")
    linhas.append(f"| Tools | {a['tools'] or 'todas'} |")
    linhas.append(f"| Seções | {' → '.join(a['cabecalhos'][:10]) or '—'} |")
    linhas.append("| Destino provável | `agent/subagents/` (contexto isolado por desenho) |\n")
    linhas.append("## Notas de migração\n")
    linhas.append((notas or "_(vazio)_") + "\n")
    return "\n".join(linhas)


def pagina_cluster(cid: str, titulo: str, membros: list[dict]) -> str:
    fm = {
        "type": "Cluster",
        "title": titulo,
        "description": f"{len(membros)} skills disputam a intenção “{titulo}”.",
        "tags": ["cluster", cid],
        "generated": {"by": ATOR, "at": agora()},
        "status": "draft",
        "related": [f"skills/{m['pasta']}" for m in membros],
        "cluster": {"id": cid, "membros": [m["pasta"] for m in membros]},
    }
    linhas = [dump_frontmatter(fm), f"# Cluster: {titulo}\n"]
    linhas.append("Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.\n")
    linhas.append("| Skill | Descrição | Scripts | Ferramentas |\n|---|---|---|---|")
    for m in membros:
        linhas.append(f"| [{m['pasta']}](../skills/{m['pasta']}.md) | {uma_linha(m['descricao'], 110)} | {len(m['scripts'])} | {', '.join(m['ferramentas'][:5])} |")
    # ferramentas em comum = candidatas a tools/
    contagem: dict[str, int] = {}
    for m in membros:
        for f in m["ferramentas"]:
            contagem[f] = contagem.get(f, 0) + 1
    comuns = [f for f, n in sorted(contagem.items(), key=lambda x: -x[1]) if n >= 2]
    linhas.append("\n## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)\n")
    linhas.append(", ".join(f"`{f}` ({contagem[f]}×)" for f in comuns) if comuns else "_nenhuma ferramenta citada por 2+ skills_")
    linhas.append("\n## Decisão de consolidação\n\n_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_\n")
    return "\n".join(linhas)


def _sem_timestamp(txt: str) -> str:
    return re.sub(r"^\s+at: .*$", "", txt, flags=re.M)


def escrever(arq: Path, conteudo: str, dry: bool) -> bool:
    """Escreve só se algo além de `generated.at` mudou (idempotente)."""
    if arq.exists() and _sem_timestamp(arq.read_text(encoding="utf-8")) == _sem_timestamp(conteudo):
        return False
    if not dry:
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_text(conteudo, encoding="utf-8")
    return True


def gerar_index(pasta: Path, titulo: str, dry: bool, extra: str = "") -> None:
    itens = []
    for arq in sorted(pasta.glob("*.md")):
        if arq.name in {"index.md", "log.md"}:
            continue
        fm, _ = split_frontmatter(arq.read_text(encoding="utf-8", errors="replace"))
        t = fm.get("title") or arq.stem
        d = uma_linha(fm.get("description") or "", 140)
        est = ""
        if isinstance(fm.get("migracao"), dict):
            est = f" · `{fm['migracao'].get('estagio', '')}`"
        itens.append(f"- [{t}]({arq.name}) — {d}{est}")
    corpo = f"# {titulo}\n\n{extra}{len(itens)} conceitos.\n\n" + "\n".join(itens) + "\n"
    escrever(pasta / "index.md", corpo, dry)


def registrar_log(wiki: Path, linha: str, dry: bool) -> None:
    arq = wiki / "log.md"
    cab = "# Log da wiki\n\nMais recente no topo. `| data | ator | ação | conceitos |`\n\n| data | ator | ação | conceitos |\n|---|---|---|---|\n"
    if arq.exists():
        txt = arq.read_text(encoding="utf-8")
        if "|---|---|---|---|" in txt:
            i = txt.index("|---|---|---|---|") + len("|---|---|---|---|\n")
            novo = txt[:i] + linha + "\n" + txt[i:]
        else:
            novo = cab + linha + "\n"
    else:
        novo = cab + linha + "\n"
    if not dry:
        arq.write_text(novo, encoding="utf-8")


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills", default=str(HOME / ".claude" / "skills"))
    ap.add_argument("--agents", default=str(HOME / ".claude" / "agents"))
    ap.add_argument("--wiki", default=str(RAIZ / "wiki"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    skills_dir, agents_dir, wiki = Path(args.skills), Path(args.agents), Path(args.wiki)
    dry = args.dry_run

    skills = [s for s in (ler_skill(d) for d in sorted(skills_dir.iterdir()) if d.is_dir()) if s]
    sem_skill_md = [d.name for d in sorted(skills_dir.iterdir()) if d.is_dir() and not (d / "SKILL.md").exists()]
    agentes = [ler_agente(a) for a in sorted(agents_dir.glob("*.md"))] if agents_dir.exists() else []

    mudados = 0
    por_cluster: dict[str, list[dict]] = {}
    for s in skills:
        arq = wiki / "skills" / f"{s['pasta']}.md"
        fm_ex, notas = carregar_existente(arq)
        cid = cluster_de(s)
        if isinstance(fm_ex.get("migracao"), dict) and fm_ex["migracao"].get("cluster"):
            cid = fm_ex["migracao"]["cluster"]  # decisão humana vence a heurística
        por_cluster.setdefault(cid, []).append(s)
        mudados += escrever(arq, pagina_skill(s, cid, fm_ex, notas), dry)

    for a in agentes:
        arq = wiki / "agentes" / f"{Path(a['path']).stem}.md"
        fm_ex, notas = carregar_existente(arq)
        mudados += escrever(arq, pagina_agente(a, fm_ex, notas), dry)

    titulos = {c["id"]: c["titulo"] for c in CLUSTERS}
    titulos["outros"] = "Outros (sem cluster — classificar manualmente)"
    for cid, membros in por_cluster.items():
        arq = wiki / "clusters" / f"{cid}.md"
        mudados += escrever(arq, pagina_cluster(cid, titulos.get(cid, cid), membros), dry)
    # remove clusters órfãos gerados anteriormente
    for arq in (wiki / "clusters").glob("*.md"):
        if arq.name not in {"index.md", "log.md"} and arq.stem not in por_cluster:
            if not dry:
                arq.unlink()
            mudados += 1

    gerar_index(wiki / "skills", "Skills instaladas", dry, "Gerado por `tools/inventario.py`. Estágio de migração entre crases.\n\n")
    gerar_index(wiki / "agentes", "Agentes instalados", dry)
    gerar_index(wiki / "clusters", "Clusters de sobreposição", dry, "Skills que disputam a mesma intenção (etapa 1 → decidir consolidação).\n\n")
    gerar_index(wiki / "conceitos", "Conceitos", dry)

    raiz = (
        "# Wiki — agentes-fronteiros\n\nBundle OKF. Comece por [SCHEMA.md](SCHEMA.md).\n\n"
        f"- [conceitos/](conceitos/index.md) — conceitos curados\n"
        f"- [skills/](skills/index.md) — {len(skills)} skills instaladas (1 conceito cada)\n"
        f"- [agentes/](agentes/index.md) — {len(agentes)} agentes\n"
        f"- [clusters/](clusters/index.md) — {len(por_cluster)} clusters de sobreposição\n"
        f"- [raw/](raw/) — fontes brutas (não editar)\n"
        f"- [log.md](log.md) — histórico\n"
    )
    if sem_skill_md:
        raiz += f"\nPastas em skills sem `SKILL.md` (ignoradas): {', '.join(sem_skill_md)}\n"
    escrever(wiki / "index.md", raiz, dry)

    if mudados:
        registrar_log(wiki, f"| {hoje()} | {ATOR} | inventário: {len(skills)} skills, {len(agentes)} agentes, {len(por_cluster)} clusters, {mudados} arquivos alterados | skills/*, agentes/*, clusters/* |", dry)

    print(f"skills: {len(skills)} (sem SKILL.md: {len(sem_skill_md)})  agentes: {len(agentes)}  clusters: {len(por_cluster)}  arquivos alterados: {mudados}{'  [dry-run]' if dry else ''}")
    for cid, membros in sorted(por_cluster.items(), key=lambda x: -len(x[1])):
        print(f"  {cid:<20} {len(membros):>3}  {', '.join(m['pasta'] for m in membros)[:110]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
