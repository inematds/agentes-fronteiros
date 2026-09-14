---
type: Skill
title: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to
  test a skill, benchmark skill…
resource: file:///home/nmaldaner/.claude/skills/skill-creator/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/skill-creator/SKILL.md
  author: human:nei
  last_modified: '2026-03-05'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 18
  subpastas:
  - agents
  - assets
  - eval-viewer
  - references
  - scripts
  scripts:
  - eval-viewer/generate_review.py
  - scripts/__init__.py
  - scripts/aggregate_benchmark.py
  - scripts/generate_report.py
  - scripts/improve_description.py
  - scripts/package_skill.py
  - scripts/quick_validate.py
  - scripts/run_eval.py
  - scripts/run_loop.py
  - scripts/utils.py
  ferramentas:
  - mcp
  - python
  gatilhos: []
  tamanho_skill_md: 32189
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# skill-creator

## Descrição (do SKILL.md)

Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | mcp, python |
| Processo (cabeçalhos) | Skill Creator → Communicating with the user → Creating a skill → Capture Intent → Interview and Research → Write the SKILL.md → Skill Writing Guide → Report structure → [Title] → Executive summary |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: agents, assets, eval-viewer, references, scripts · SKILL.md com 32,189 chars |

## Scripts (candidatos a `agent/tools/`)

- `eval-viewer/generate_review.py`
- `scripts/__init__.py`
- `scripts/aggregate_benchmark.py`
- `scripts/generate_report.py`
- `scripts/improve_description.py`
- `scripts/package_skill.py`
- `scripts/quick_validate.py`
- `scripts/run_eval.py`
- `scripts/run_loop.py`
- `scripts/utils.py`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
