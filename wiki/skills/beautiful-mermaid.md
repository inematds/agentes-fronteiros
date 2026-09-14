---
type: Skill
title: beautiful-mermaid
description: Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram.
resource: file:///home/nmaldaner/.claude/skills/beautiful-mermaid/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/beautiful-mermaid/SKILL.md
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
  arquivos: 4
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/create-html.ts
  - scripts/render.ts
  ferramentas:
  - agent-browser
  - github
  - node
  gatilhos: []
  tamanho_skill_md: 5154
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# beautiful-mermaid

## Descrição (do SKILL.md)

Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram. |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | agent-browser, github, node |
| Processo (cabeçalhos) | Beautiful Mermaid Diagram Rendering → Dependencies → Supported Diagram Types → Available Themes → Common Syntax Patterns → Flowchart Edge Labels → Node Labels with Special Characters → Workflow → Step 1: Generate or Validate Mermaid Code → Step 2: Render SVG |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 5,154 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/create-html.ts`
- `scripts/render.ts`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
