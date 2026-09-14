#!/usr/bin/env python3
"""
wiki_lint.py — valida o bundle OKF em wiki/.

Falha (exit 1) quando:
  - um conceito (qualquer .md fora index.md/log.md/raw/) não tem frontmatter ou não tem `type`;
  - index.md ou log.md carrega frontmatter de conceito (`type`);
  - um link markdown relativo aponta para arquivo inexistente;
  - `related:` cita um concept ID que não existe;
  - `migracao.estagio` tem valor fora da lista;
  - `status` fora de draft|stable|deprecated.

Uso: python3 tools/wiki_lint.py [--wiki DIR]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ESTAGIOS = {"inventariado", "mapeado", "skill", "tools", "contrato", "loop", "testado", "aprovado", "descontinuado"}
STATUS = {"draft", "stable", "deprecated"}
RESERVADOS = {"index.md", "log.md"}


def frontmatter(texto: str) -> dict | None:
    if not texto.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", texto, re.S)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return {"__erro__": str(e)}
    return fm if isinstance(fm, dict) else {"__erro__": "frontmatter não é um mapa"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default=str(RAIZ / "wiki"))
    args = ap.parse_args()
    wiki = Path(args.wiki)

    erros: list[str] = []
    avisos: list[str] = []
    conceitos = 0
    ids: set[str] = set()

    arquivos = [p for p in wiki.rglob("*.md") if "raw" not in p.relative_to(wiki).parts]
    for p in arquivos:
        if p.name not in RESERVADOS:
            ids.add(str(p.relative_to(wiki).with_suffix("")))

    for p in arquivos:
        rel = p.relative_to(wiki)
        texto = p.read_text(encoding="utf-8", errors="replace")
        fm = frontmatter(texto)

        if p.name in RESERVADOS:
            if fm and fm.get("type"):
                erros.append(f"{rel}: arquivo reservado não pode ser conceito (tem `type`)")
        else:
            conceitos += 1
            if fm is None:
                erros.append(f"{rel}: sem frontmatter")
            elif "__erro__" in fm:
                erros.append(f"{rel}: frontmatter inválido — {fm['__erro__']}")
            else:
                if not fm.get("type"):
                    erros.append(f"{rel}: falta `type` (único campo obrigatório do OKF)")
                st = fm.get("status")
                if st and st not in STATUS:
                    erros.append(f"{rel}: status `{st}` fora de {sorted(STATUS)}")
                mig = fm.get("migracao")
                if isinstance(mig, dict):
                    est = mig.get("estagio")
                    if est not in ESTAGIOS:
                        erros.append(f"{rel}: migracao.estagio `{est}` inválido")
                for r in fm.get("related") or []:
                    if str(r) not in ids:
                        erros.append(f"{rel}: related `{r}` não existe")
                if not fm.get("generated"):
                    avisos.append(f"{rel}: sem `generated` (proveniência desconhecida)")
                if not fm.get("description"):
                    avisos.append(f"{rel}: sem `description`")

        # links relativos (ignorando código inline e blocos)
        sem_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
        sem_codigo = re.sub(r"`[^`\n]*`", "", sem_codigo)
        for alvo in re.findall(r"\]\(([^)\s#]+)(?:#[^)]*)?\)", sem_codigo):
            if re.match(r"^[a-z]+:", alvo):
                continue
            destino = (p.parent / alvo).resolve()
            if not destino.exists():
                erros.append(f"{rel}: link quebrado → {alvo}")

    print(f"wiki: {conceitos} conceitos · {len(erros)} erros · {len(avisos)} avisos")
    for e in erros:
        print(f"  ERRO  {e}")
    for a in avisos[:30]:
        print(f"  aviso {a}")
    if len(avisos) > 30:
        print(f"  … +{len(avisos) - 30} avisos")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
