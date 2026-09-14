---
type: Skill
title: media-use
description: Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready
  block + ledger record (one ve…
resource: file:///home/nmaldaner/.claude/skills/media-use/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/media-use/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 158
  subpastas:
  - audio
  - luts
  - references
  - scripts
  scripts:
  - audio/scripts/audio.mjs
  - audio/scripts/audio.test.mjs
  - audio/scripts/heygen-tts.mjs
  - audio/scripts/lib/audio-meta.mjs
  - audio/scripts/lib/audio-meta.test.mjs
  - audio/scripts/lib/bgm.mjs
  - audio/scripts/lib/bgm.test.mjs
  - audio/scripts/lib/concurrency.mjs
  - audio/scripts/lib/concurrency.test.mjs
  - audio/scripts/lib/heygen.mjs
  - audio/scripts/lib/heygen.test.mjs
  - audio/scripts/lib/python.mjs
  - audio/scripts/lib/python.test.mjs
  - audio/scripts/lib/sfx.mjs
  - audio/scripts/lib/sfx.test.mjs
  - audio/scripts/lib/tts.mjs
  - audio/scripts/lib/tts.spawn.test.mjs
  - audio/scripts/lib/tts.test.mjs
  - audio/scripts/lyria-recipe.py
  - audio/scripts/wait-bgm.mjs
  - audio/scripts/wait-bgm.test.mjs
  - scripts/audio-duck.mjs
  - scripts/dither.mjs
  - scripts/dither.test.mjs
  - scripts/eval.mjs
  - scripts/lib/adopt.mjs
  - scripts/lib/adopt.test.mjs
  - scripts/lib/bgm-provider.mjs
  - scripts/lib/brand-provider.mjs
  - scripts/lib/bundled-sfx-provider.mjs
  ferramentas:
  - github
  - heygen
  - hyperframes
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 7951
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# media-use

## Descrição (do SKILL.md)

Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block + ledger record (one verb, `resolve`); generate via TTS / music / image models when the catalog misses; produce voiceover, transcription, captions, and background removal through one shared audio engine; operate on media (cut / reframe / transform); and reuse assets across projects. Also use for vague feedback that real footage looks dark, flat, boring, should feel retro/camcorder/print/ASCII, needs privacy, or needs a media reveal.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a fr… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, heygen, hyperframes, node, tts |
| Processo (cabeçalhos) | media-use → Resolve — the one verb → Treat broad visual feedback as media intent → Be proactive — run a media opportunity pass → Where to look — read only the file your task needs |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: audio, luts, references, scripts · SKILL.md com 7,951 chars |

## Scripts (candidatos a `agent/tools/`)

- `audio/scripts/audio.mjs`
- `audio/scripts/audio.test.mjs`
- `audio/scripts/heygen-tts.mjs`
- `audio/scripts/lib/audio-meta.mjs`
- `audio/scripts/lib/audio-meta.test.mjs`
- `audio/scripts/lib/bgm.mjs`
- `audio/scripts/lib/bgm.test.mjs`
- `audio/scripts/lib/concurrency.mjs`
- `audio/scripts/lib/concurrency.test.mjs`
- `audio/scripts/lib/heygen.mjs`
- `audio/scripts/lib/heygen.test.mjs`
- `audio/scripts/lib/python.mjs`
- `audio/scripts/lib/python.test.mjs`
- `audio/scripts/lib/sfx.mjs`
- `audio/scripts/lib/sfx.test.mjs`
- `audio/scripts/lib/tts.mjs`
- `audio/scripts/lib/tts.spawn.test.mjs`
- `audio/scripts/lib/tts.test.mjs`
- `audio/scripts/lyria-recipe.py`
- `audio/scripts/wait-bgm.mjs`
- `audio/scripts/wait-bgm.test.mjs`
- `scripts/audio-duck.mjs`
- `scripts/dither.mjs`
- `scripts/dither.test.mjs`
- `scripts/eval.mjs`
- `scripts/lib/adopt.mjs`
- `scripts/lib/adopt.test.mjs`
- `scripts/lib/bgm-provider.mjs`
- `scripts/lib/brand-provider.mjs`
- `scripts/lib/bundled-sfx-provider.mjs`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
