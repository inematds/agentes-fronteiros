---
type: Skill
title: os-coach
description: Hand-holds a non-technical person through building and assessing their own agentic OS, one layer at a time. Remembers exactly where they are in memory.md and gives goal-grounded, non-generic
  audits on demand. Trigger wi…
resource: file:///home/nmaldaner/.claude/skills/os-coach/SKILL.md
tags:
- skill
- conselho
sources:
- path: /home/nmaldaner/.claude/skills/os-coach/SKILL.md
  author: human:nei
  last_modified: '2026-07-03'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/conselho
skill:
  versao: ''
  invocacao_pelo_modelo: false
  arquivos: 11
  subpastas:
  - assets
  - references
  scripts:
  - assets/gen_diagrams.py
  ferramentas: []
  gatilhos: []
  tamanho_skill_md: 9233
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# os-coach

## Descrição (do SKILL.md)

Hand-holds a non-technical person through building and assessing their own agentic OS, one layer at a time. Remembers exactly where they are in memory.md and gives goal-grounded, non-generic audits on demand. Trigger with /os-coach.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Hand-holds a non-technical person through building and assessing their own agentic OS, one layer at a time. Remembers exactly where they are in memory.md and g… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | — |
| Processo (cabeçalhos) | OS Coach → Live state (loaded for you) → What the user asked → Golden rules (never break these) → Guards (check before running any flow) → The Start flow → Coach a layer flow → Audit flow → memory.md schema → OS Coach Memory |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 9,233 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/gen_diagrams.py`

## Cluster

[conselho](../clusters/conselho.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
