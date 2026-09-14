#!/usr/bin/env python3
"""
server.py — interface de migração (servidor local, só stdlib + PyYAML).

A wiki (bundle OKF) é a única fonte de verdade: o estágio de migração de cada
skill mora no frontmatter `migracao:` de wiki/skills/<nome>.md.

Endpoints:
  GET  /                      index.html
  GET  /api/inventario        skills + agentes (frontmatter das páginas da wiki)
  GET  /api/clusters          clusters e membros
  GET  /api/contratos         contratos YAML em migracao/contratos/
  GET  /api/wiki?id=<concept> markdown bruto de um conceito (id sem .md)
  GET  /api/log               wiki/log.md
  POST /api/migracao          {id, estagio?, cluster?, destino?, notas?} → atualiza frontmatter + log
  POST /api/rescan            roda tools/inventario.py

Uso: python3 interface/server.py [--port 8765]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

RAIZ = Path(__file__).resolve().parent.parent
WIKI = RAIZ / "wiki"
CONTRATOS = RAIZ / "migracao" / "contratos"
HTML = Path(__file__).resolve().parent / "index.html"
ESTAGIOS = ["inventariado", "mapeado", "skill", "tools", "contrato", "loop", "testado", "aprovado", "descontinuado"]
ATOR = "interface/server.py"


def split_fm(texto: str) -> tuple[dict, str, str]:
    """(frontmatter, corpo, bloco_fm_original)"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", texto, re.S)
    if not m:
        return {}, texto, ""
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), texto[m.end():], m.group(0)


def dump_fm(fm: dict) -> str:
    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=200).rstrip() + "\n---\n"


def ler_conceito(arq: Path) -> dict:
    fm, corpo, _ = split_fm(arq.read_text(encoding="utf-8", errors="replace"))
    cid = str(arq.relative_to(WIKI).with_suffix(""))
    return {"id": cid, "arquivo": str(arq), **fm}


def listar(pasta: str) -> list[dict]:
    p = WIKI / pasta
    if not p.exists():
        return []
    return [ler_conceito(a) for a in sorted(p.glob("*.md")) if a.name not in {"index.md", "log.md"}]


def inventario() -> dict:
    skills = listar("skills")
    agentes = listar("agentes")
    por_estagio = {e: 0 for e in ESTAGIOS}
    for s in skills + agentes:
        est = (s.get("migracao") or {}).get("estagio", "inventariado")
        por_estagio[est] = por_estagio.get(est, 0) + 1
    return {"skills": skills, "agentes": agentes, "estagios": ESTAGIOS, "por_estagio": por_estagio,
            "gerado_em": dt.datetime.now().isoformat(timespec="seconds")}


def clusters() -> list[dict]:
    return listar("clusters")


def contratos() -> list[dict]:
    out = []
    for arq in sorted(CONTRATOS.glob("*.yaml")):
        try:
            data = yaml.safe_load(arq.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            data = {"erro": str(e)}
        out.append({"arquivo": arq.name, "raw": arq.read_text(encoding="utf-8"), **(data if isinstance(data, dict) else {})})
    return out


def registrar_log(linha: str) -> None:
    arq = WIKI / "log.md"
    marca = "|---|---|---|---|\n"
    txt = arq.read_text(encoding="utf-8") if arq.exists() else "# Log da wiki\n\n| data | ator | ação | conceitos |\n" + marca
    if marca in txt:
        i = txt.index(marca) + len(marca)
        txt = txt[:i] + linha + "\n" + txt[i:]
    else:
        txt += linha + "\n"
    arq.write_text(txt, encoding="utf-8")


def atualizar_migracao(payload: dict) -> dict:
    cid = str(payload.get("id", ""))
    if not re.match(r"^(skills|agentes)/[A-Za-z0-9._-]+$", cid):
        raise ValueError("id inválido")
    arq = WIKI / f"{cid}.md"
    if not arq.exists():
        raise FileNotFoundError(f"não encontrado: {cid}")
    texto = arq.read_text(encoding="utf-8")
    fm, corpo, bloco = split_fm(texto)
    if not bloco:
        raise ValueError("página sem frontmatter")
    mig = dict(fm.get("migracao") or {})
    mudou = []
    for campo in ("estagio", "cluster", "destino", "notas"):
        if campo in payload and payload[campo] is not None:
            val = str(payload[campo]).strip()
            if campo == "estagio" and val not in ESTAGIOS:
                raise ValueError(f"estágio inválido: {val}")
            if mig.get(campo, "") != val:
                mig[campo] = val
                mudou.append(f"{campo}={val[:40]}")
    if not mudou:
        return {"ok": True, "mudou": False, "migracao": mig}
    mig["atualizado"] = dt.date.today().isoformat()
    fm["migracao"] = mig
    # mantém tags/related coerentes com o cluster
    if "cluster" in payload and mig.get("cluster"):
        tags = [t for t in (fm.get("tags") or []) if t not in {c["id"].split("/")[-1] for c in clusters()}]
        fm["tags"] = tags + [mig["cluster"]] if mig["cluster"] not in tags else tags
        rel = [r for r in (fm.get("related") or []) if not str(r).startswith("clusters/")]
        fm["related"] = rel + [f"clusters/{mig['cluster']}"]
    arq.write_text(dump_fm(fm) + corpo, encoding="utf-8")
    registrar_log(f"| {dt.date.today().isoformat()} | {ATOR} | migração: {', '.join(mudou)} | {cid} |")
    return {"ok": True, "mudou": True, "migracao": mig}


def rescan() -> dict:
    r = subprocess.run([sys.executable, str(RAIZ / "tools" / "inventario.py")], capture_output=True, text=True, timeout=120)
    return {"ok": r.returncode == 0, "stdout": r.stdout[-4000:], "stderr": r.stderr[-2000:]}


class H(BaseHTTPRequestHandler):
    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _text(self, s: str, ctype="text/plain; charset=utf-8", code=200):
        b = s.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, fmt, *args):  # silencioso, exceto erros
        if args and str(args[1]).startswith(("4", "5")):
            super().log_message(fmt, *args)

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        try:
            if u.path in ("/", "/index.html"):
                return self._text(HTML.read_text(encoding="utf-8"), "text/html; charset=utf-8")
            if u.path == "/api/inventario":
                return self._json(inventario())
            if u.path == "/api/clusters":
                return self._json(clusters())
            if u.path == "/api/contratos":
                return self._json(contratos())
            if u.path == "/api/log":
                return self._text((WIKI / "log.md").read_text(encoding="utf-8") if (WIKI / "log.md").exists() else "")
            if u.path == "/api/wiki":
                cid = q.get("id", [""])[0]
                if not re.match(r"^[A-Za-z0-9._/-]+$", cid) or ".." in cid:
                    return self._json({"erro": "id inválido"}, 400)
                arq = WIKI / f"{cid}.md"
                if not arq.exists():
                    return self._json({"erro": "não encontrado"}, 404)
                return self._text(arq.read_text(encoding="utf-8"), "text/markdown; charset=utf-8")
            return self._json({"erro": "rota"}, 404)
        except Exception as e:  # noqa: BLE001
            return self._json({"erro": str(e)}, 500)

    def do_POST(self):
        u = urlparse(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b"{}"
        try:
            payload = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return self._json({"erro": "json inválido"}, 400)
        try:
            if u.path == "/api/migracao":
                return self._json(atualizar_migracao(payload))
            if u.path == "/api/rescan":
                return self._json(rescan())
            return self._json({"erro": "rota"}, 404)
        except (ValueError, FileNotFoundError) as e:
            return self._json({"erro": str(e)}, 400)
        except Exception as e:  # noqa: BLE001
            return self._json({"erro": str(e)}, 500)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    a = ap.parse_args()
    srv = ThreadingHTTPServer((a.host, a.port), H)
    print(f"interface de migração: http://{a.host}:{a.port}  (wiki: {WIKI})")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
