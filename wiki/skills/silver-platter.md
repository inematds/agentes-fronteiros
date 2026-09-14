---
type: Skill
title: silver-platter
description: Interview a business owner about their day-to-day tools, build a tailored data map, render a Pantry → Prep → Plate HTML visualization with recipes, a 30-day build plan, and an interaction-layer
  Sankey, plus generate pla…
resource: file:///home/nmaldaner/.claude/skills/silver-platter/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/silver-platter/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 60
  subpastas:
  - examples
  - references
  - scripts
  scripts:
  - scripts/audit_existing_folder.py
  - scripts/render_data_map.py
  ferramentas:
  - mcp
  - python
  - telegram
  gatilhos: []
  tamanho_skill_md: 24908
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# silver-platter

## Descrição (do SKILL.md)

Interview a business owner about their day-to-day tools, build a tailored data map, render a Pantry → Prep → Plate HTML visualization with recipes, a 30-day build plan, and an interaction-layer Sankey, plus generate plain-English Claude Code recommendations (skills, subagents, hooks, rules, CLIs to install). Audits existing Claude Code setups in the cwd before asking questions, so users who've started building don't get re-asked. Output: a self-contained data_map.html, an OPPORTUNITIES.md, and a copy-paste prompt for the @claude-code-guide agent. Free, open-source, ships in the Business OS Demos Kit.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Interview a business owner about their day-to-day tools, build a tailored data map, render a Pantry → Prep → Plate HTML visualization with recipes, a 30-day bu… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | mcp, python, telegram |
| Processo (cabeçalhos) | /silver-platter → Hard rules (non-negotiable) → How you work → Stage 0, silent audit (no operator prompt yet) → Stage 1, greet and pick speed → Stage 2, business archetype → Stage 3, Pantry tools (DO NOT ask schema fields) → Stage 4, existing automation audit → Stage 5, data-engineering reality check → Stage 6, assemble Pantry / Prep / Plate |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: examples, references, scripts · SKILL.md com 24,908 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/audit_existing_folder.py`
- `scripts/render_data_map.py`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
