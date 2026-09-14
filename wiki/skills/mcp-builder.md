---
type: Skill
title: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate
  external APIs or services,…
resource: file:///home/nmaldaner/.claude/skills/mcp-builder/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/mcp-builder/SKILL.md
  author: human:nei
  last_modified: '2026-03-11'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 10
  subpastas:
  - reference
  - scripts
  scripts:
  - scripts/connections.py
  - scripts/evaluation.py
  ferramentas:
  - github
  - mcp
  - node
  - python
  gatilhos: []
  tamanho_skill_md: 9059
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# mcp-builder

## Descrição (do SKILL.md)

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, mcp, node, python |
| Processo (cabeçalhos) | MCP Server Development Guide → Overview → Process → 🚀 High-Level Workflow → Phase 1: Deep Research and Planning → Phase 2: Implementation → Phase 3: Review and Test → Phase 4: Create Evaluations → Reference Files → 📚 Documentation Library |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: reference, scripts · SKILL.md com 9,059 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/connections.py`
- `scripts/evaluation.py`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
