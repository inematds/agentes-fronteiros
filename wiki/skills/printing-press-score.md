---
type: Skill
title: printing-press-score
description: Score a generated CLI against the Steinberger bar, compare two CLIs side-by-side
resource: file:///home/nmaldaner/.claude/skills/printing-press-score/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-score/SKILL.md
  author: human:nei
  last_modified: '2026-05-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/printing-press
skill:
  versao: 0.1.0
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - github
  gatilhos: []
  tamanho_skill_md: 9826
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-score

## Descrição (do SKILL.md)

Score a generated CLI against the Steinberger bar, compare two CLIs side-by-side

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Score a generated CLI against the Steinberger bar, compare two CLIs side-by-side |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github |
| Processo (cabeçalhos) | /printing-press-score → Quick Start → Prerequisites → Step 0: Setup → min-binary-version: 4.0.0 → Derive scope first — needed for local build detection → Prefer local build when running from inside the printing-press repo. → Step 1: Parse Arguments → Step 2: Resolve CLI Directories → If the token contains `/` or `.` |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 9,826 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
