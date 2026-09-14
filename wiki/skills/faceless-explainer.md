---
type: Skill
title: faceless-explainer
description: 'Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per scene (typography, abstract
  graphics, diagrams, data-v…'
resource: file:///home/nmaldaner/.claude/skills/faceless-explainer/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/faceless-explainer/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-explicativo
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 24
  subpastas:
  - references
  - scripts
  - sub-agents
  scripts:
  - scripts/assemble-index.mjs
  - scripts/assemble-index.test.mjs
  - scripts/audio.mjs
  - scripts/audio.test.mjs
  - scripts/build-frame.mjs
  - scripts/captions.mjs
  - scripts/captions.test.mjs
  - scripts/frame-packets.mjs
  - scripts/frame-packets.test.mjs
  - scripts/lib/assets.mjs
  - scripts/lib/dimensions.mjs
  - scripts/lib/pad-frame-duration.mjs
  - scripts/lib/storyboard.mjs
  - scripts/lib/tokens.mjs
  - scripts/lib/transition-registry.mjs
  - scripts/transitions.mjs
  - scripts/transitions.test.mjs
  ferramentas:
  - github
  - heygen
  - hyperframes
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 29476
migracao:
  estagio: inventariado
  cluster: video-explicativo
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# faceless-explainer

## Descrição (do SKILL.md)

Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per scene (typography, abstract graphics, diagrams, data-viz). Use for topic explainers, concept breakdowns, how-tos, listicles. Not a video built from a website (/product-launch-video — promo or tour). Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invente… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, heygen, hyperframes, node, tts |
| Processo (cabeçalhos) | Faceless Explainer to HyperFrames → Step 0: Setup → Step 1: Brief (no capture) → Step 2: Design System → Step 3: Storyboard and Script → Step 3.1: Audio → Step 4: Frame Visual Design → Step 5: Build Frames → Step 6: Finalize → Quick Reference |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts, sub-agents · SKILL.md com 29,476 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/assemble-index.mjs`
- `scripts/assemble-index.test.mjs`
- `scripts/audio.mjs`
- `scripts/audio.test.mjs`
- `scripts/build-frame.mjs`
- `scripts/captions.mjs`
- `scripts/captions.test.mjs`
- `scripts/frame-packets.mjs`
- `scripts/frame-packets.test.mjs`
- `scripts/lib/assets.mjs`
- `scripts/lib/dimensions.mjs`
- `scripts/lib/pad-frame-duration.mjs`
- `scripts/lib/storyboard.mjs`
- `scripts/lib/tokens.mjs`
- `scripts/lib/transition-registry.mjs`
- `scripts/transitions.mjs`
- `scripts/transitions.test.mjs`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
