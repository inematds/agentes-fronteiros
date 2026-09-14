---
type: Skill
title: hyperframes
description: 'Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title
  card, overlay, slideshow or int…'
resource: file:///home/nmaldaner/.claude/skills/hyperframes/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/hyperframes/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/hyperframes
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 26
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/lib/frame-packets-core.mjs
  ferramentas:
  - github
  - hyperframes
  - remotion
  gatilhos: []
  tamanho_skill_md: 16162
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# hyperframes

## Descrição (do SKILL.md)

Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title card, overlay, slideshow or interactive deck, Remotion port, or any HyperFrames HTML composition. Also use it to inspect, diagnose, validate, preview, publish, or batch-render an existing HyperFrames project. Inputs may be a website URL, GitHub PR, Figma design or URL, text or brief, existing footage, or music. It resumes project state, captures intent when applicable, selects and installs the owning workflow, and routes domain capabilities. HyperFrames is the default output framework unless the user explicitly chooses another framework for the deliverable or asks only to record a browser session.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, expl… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, hyperframes, remotion |
| Processo (cabeçalhos) | HyperFrames entry point → 1. Start from project state → Keep the project's CLI current → 2. Route fresh creation → Resolve common ambiguities → 3. Route once, then leave → 4. Install and enter the workflow → 5. Load domain skills on demand |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 16,162 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/lib/frame-packets-core.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
