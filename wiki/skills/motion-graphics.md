---
type: Skill
title: motion-graphics
description: A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout / social overlay, animated
  map (highlight regions,…
resource: file:///home/nmaldaner/.claude/skills/motion-graphics/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/motion-graphics/SKILL.md
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
  arquivos: 23
  subpastas:
  - agents
  - categories
  - grounding
  - phases
  - references
  - samples
  scripts:
  - categories/maps/bake-basemap.mjs
  - grounding/locate.mjs
  ferramentas:
  - ffmpeg
  - gemini
  - github
  - hyperframes
  - mcp
  - node
  - remotion
  gatilhos: []
  tamanho_skill_md: 15566
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# motion-graphics

## Descrição (do SKILL.md)

A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout / social overlay, animated map (highlight regions, connect places, zoom to a location), animated tweet / news-article / headline, webpage / UI animation (scroll, cursor, callouts), or fusing a real image's geometry into a chart. Usually under 10s (up to ~30s), no narration or live-action subject; renders to MP4 or transparent overlay. Longer / narrated / multi-scene → /general-video. Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | ffmpeg, gemini, github, hyperframes, mcp, node, remotion |
| Processo (cabeçalhos) | motion-graphics — dispatch entry → Categories — split by the search decision → Prerequisites → Flow → Step 0 — Initialize → Step 1 — Plan (subagent: Director Part 1) → Step 2 — Source ◇ (Bash: media-use, conditional) → illustrative — see phases/source/guide.md → Step 3 — Design (subagent: Director Part 2) → Step 4 — Build (subagent: Builder, reuse-first) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: agents, categories, grounding, phases, references, samples · SKILL.md com 15,566 chars |

## Scripts (candidatos a `agent/tools/`)

- `categories/maps/bake-basemap.mjs`
- `grounding/locate.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
