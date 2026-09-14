---
type: Skill
title: printing-press-import
description: Bring a published CLI from the public library into the internal library so it's identical to a freshly-generated copy — module path reverted, manuscripts placed alongside, ready for /printing-press-polish
  or /printing-p…
resource: file:///home/nmaldaner/.claude/skills/printing-press-import/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-import/SKILL.md
  author: human:nei
  last_modified: '2026-05-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/printing-press
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 5
  subpastas:
  - references
  scripts:
  - references/import-backup.sh
  - references/import-fetch.sh
  - references/import-place.sh
  - references/import-rewrite.sh
  ferramentas:
  - github
  gatilhos:
  - import the CLI
  - bring it into my library
  - fetch from public library
  - I don't have it locally yet
  tamanho_skill_md: 7729
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-import

## Descrição (do SKILL.md)

Bring a published CLI from the public library into the internal library so it's identical to a freshly-generated copy — module path reverted, manuscripts placed alongside, ready for /printing-press-polish or /printing-press-emboss. Use when the public library has a CLI you don't have locally, or to recover from a broken/lost internal copy. Trigger phrases: "import the CLI", "bring it into my library", "fetch from public library", "I don't have it locally yet".


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Bring a published CLI from the public library into the internal library so it's identical to a freshly-generated copy — module path reverted, manuscripts place… |
| Entradas (gatilhos) | import the CLI, bring it into my library, fetch from public library, I don't have it locally yet |
| Ferramentas citadas | github |
| Processo (cabeçalhos) | /printing-press-import → When to run → Setup → Phase 1 — Resolve the CLI → Exact: → Normalized exact (after $ARG2 = lowercase, dot→hyphen, suffix-stripped): → Fuzzy (substring on name or description): → Phase 2 — Decide on overwrite → Internal provenance (if present): → Public provenance (one-shot via raw): |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 7,729 chars |

## Scripts (candidatos a `agent/tools/`)

- `references/import-backup.sh`
- `references/import-fetch.sh`
- `references/import-place.sh`
- `references/import-rewrite.sh`

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
