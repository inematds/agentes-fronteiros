---
type: Skill
title: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring
  state management, routing, or…
resource: file:///home/nmaldaner/.claude/skills/web-artifacts-builder/SKILL.md
tags:
- skill
- publicacao
sources:
- path: /home/nmaldaner/.claude/skills/web-artifacts-builder/SKILL.md
  author: human:nei
  last_modified: '2026-03-28'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/publicacao
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 5
  subpastas:
  - scripts
  scripts:
  - scripts/bundle-artifact.sh
  - scripts/init-artifact.sh
  ferramentas:
  - node
  - playwright
  gatilhos: []
  tamanho_skill_md: 3087
migracao:
  estagio: inventariado
  cluster: publicacao
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# web-artifacts-builder

## Descrição (do SKILL.md)

Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use fo… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | node, playwright |
| Processo (cabeçalhos) | Web Artifacts Builder → Design & Style Guidelines → Quick Start → Step 1: Initialize Project → Step 2: Develop Your Artifact → Step 3: Bundle to Single HTML File → Step 4: Share Artifact with User → Step 5: Testing/Visualizing the Artifact (Optional) → Reference |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 3,087 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/bundle-artifact.sh`
- `scripts/init-artifact.sh`

## Cluster

[publicacao](../clusters/publicacao.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
