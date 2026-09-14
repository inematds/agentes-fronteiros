---
type: Skill
title: product-launch-video
description: Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants
  to market, launch, promote, o…
resource: file:///home/nmaldaner/.claude/skills/product-launch-video/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/product-launch-video/SKILL.md
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
  arquivos: 30
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
  - scripts/capture-skill-guardrails.test.mjs
  - scripts/frame-packets.mjs
  - scripts/frame-packets.test.mjs
  - scripts/lib/assets.mjs
  - scripts/lib/dimensions.mjs
  - scripts/lib/pad-frame-duration.mjs
  - scripts/lib/pad-frame-duration.test.mjs
  - scripts/lib/storyboard.mjs
  - scripts/lib/tokens.mjs
  - scripts/lib/tokens.test.mjs
  - scripts/lib/transition-registry.mjs
  - scripts/media-contract.test.mjs
  - scripts/stage-assets.mjs
  - scripts/stage-assets.test.mjs
  - scripts/transitions.mjs
  - scripts/transitions.test.mjs
  ferramentas:
  - gemini
  - github
  - heygen
  - hyperframes
  - mcp
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 32560
migracao:
  estagio: inventariado
  cluster: video-explicativo
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# product-launch-video

## Descrição (do SKILL.md)

Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants to market, launch, promote, or reveal a product; the default for any commercial URL. Site tours / showcases of a website route here too — the brief carries the show-it-as-is intent. Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company lau… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | gemini, github, heygen, hyperframes, mcp, node, tts |
| Processo (cabeçalhos) | Product Launch to HyperFrames → Step 0: Setup → Step 1: Capture assets → Step 2: Design System → Step 3: Storyboard and Script → Step 3.1: Audio → Step 4: Frame Visual Design → Step 5: Build Frames → Step 6: Finalize → Quick Reference |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts, sub-agents · SKILL.md com 32,560 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/assemble-index.mjs`
- `scripts/assemble-index.test.mjs`
- `scripts/audio.mjs`
- `scripts/audio.test.mjs`
- `scripts/build-frame.mjs`
- `scripts/captions.mjs`
- `scripts/captions.test.mjs`
- `scripts/capture-skill-guardrails.test.mjs`
- `scripts/frame-packets.mjs`
- `scripts/frame-packets.test.mjs`
- `scripts/lib/assets.mjs`
- `scripts/lib/dimensions.mjs`
- `scripts/lib/pad-frame-duration.mjs`
- `scripts/lib/pad-frame-duration.test.mjs`
- `scripts/lib/storyboard.mjs`
- `scripts/lib/tokens.mjs`
- `scripts/lib/tokens.test.mjs`
- `scripts/lib/transition-registry.mjs`
- `scripts/media-contract.test.mjs`
- `scripts/stage-assets.mjs`
- `scripts/stage-assets.test.mjs`
- `scripts/transitions.mjs`
- `scripts/transitions.test.mjs`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
