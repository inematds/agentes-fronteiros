---
type: Skill
title: excalidraw-diagram-generator
description: Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process", "draw a system architecture", "create a mind
  map", or "generate an Excali…
resource: file:///home/nmaldaner/.claude/skills/excalidraw-diagram-generator/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/excalidraw-diagram-generator/SKILL.md
  author: human:nei
  last_modified: '2026-03-30'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 15
  subpastas:
  - references
  - scripts
  - templates
  scripts:
  - scripts/add-arrow.py
  - scripts/add-icon-to-diagram.py
  - scripts/split-excalidraw-library.py
  ferramentas:
  - node
  - python
  gatilhos:
  - create a diagram
  - make a flowchart
  - visualize a process
  - draw a system architecture
  - create a mind map
  - generate an Excalidraw file
  tamanho_skill_md: 23689
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# excalidraw-diagram-generator

## Descrição (do SKILL.md)

Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process", "draw a system architecture", "create a mind map", or "generate an Excalidraw file". Supports flowcharts, relationship diagrams, mind maps, and system architecture diagrams. Outputs .excalidraw JSON files that can be opened directly in Excalidraw.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process", "draw a syste… |
| Entradas (gatilhos) | create a diagram, make a flowchart, visualize a process, draw a system architecture, create a mind map, generate an Excalidraw file |
| Ferramentas citadas | node, python |
| Processo (cabeçalhos) | Excalidraw Diagram Generator → When to Use This Skill → Prerequisites → Step-by-Step Workflow → Step 1: Understand the Request → Step 2: Choose the Appropriate Diagram Type → Step 3: Extract Structured Information → Step 4: Generate the Excalidraw JSON → Step 5: Format the Output → Step 6: Save and Provide Instructions |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts, templates · SKILL.md com 23,689 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/add-arrow.py`
- `scripts/add-icon-to-diagram.py`
- `scripts/split-excalidraw-library.py`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
