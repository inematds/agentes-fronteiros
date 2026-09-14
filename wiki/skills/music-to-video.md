---
type: Skill
title: music-to-video
description: Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. The music drives
  all pacing; any user-supplied…
resource: file:///home/nmaldaner/.claude/skills/music-to-video/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/music-to-video/SKILL.md
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
  arquivos: 132
  subpastas:
  - references
  - scripts
  - sub-agents
  scripts:
  - references/motion-primitives/assets/gsap.min.js
  - scripts/analyze-beatgrid.py
  - scripts/assemble-index.mjs
  - scripts/lib/storyboard.mjs
  - scripts/stage-assets.mjs
  - scripts/validate-plan.mjs
  ferramentas:
  - github
  - hyperframes
  - node
  - python
  gatilhos: []
  tamanho_skill_md: 18167
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# music-to-video

## Descrição (do SKILL.md)

Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. The music drives all pacing; any user-supplied images/videos are cut onto the same beat grid, and a complete video needs zero assets. Narrated pieces → the input-matched workflow (see /hyperframes). Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or ki… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, hyperframes, node, python |
| Processo (cabeçalhos) | music-to-video — one music-grounded, beat-synced video workflow → Two ideas that shape everything → Step 0: Setup, BGM, and inputs → only if the user gave you images/videos: → Step 1: Analyze the music → Step 2: Frame skeleton (structure only) → Step 3: Fill the plan (user-gated) → Step 4: Build frames from the plan → Step 5: Assemble → Step 6: Verify and render |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts, sub-agents · SKILL.md com 18,167 chars |

## Scripts (candidatos a `agent/tools/`)

- `references/motion-primitives/assets/gsap.min.js`
- `scripts/analyze-beatgrid.py`
- `scripts/assemble-index.mjs`
- `scripts/lib/storyboard.mjs`
- `scripts/stage-assets.mjs`
- `scripts/validate-plan.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
