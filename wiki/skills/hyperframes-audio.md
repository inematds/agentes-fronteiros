---
type: Skill
title: hyperframes-audio
description: 'Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover
  (voiceover carve), effects…'
resource: file:///home/nmaldaner/.claude/skills/hyperframes-audio/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/hyperframes-audio/SKILL.md
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
  arquivos: 7
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/carve.mjs
  - scripts/carve.test.mjs
  ferramentas:
  - ffmpeg
  - hyperframes
  - node
  gatilhos: []
  tamanho_skill_md: 25400
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# hyperframes-audio

## Descrição (do SKILL.md)

Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover (voiceover carve), effects on a track (EQ, compressor, limiter, gate, saturation, delay, reverb, chorus, phaser, bitcrush), automation envelopes drawn on a track's volume or any effect parameter, or one submix bus carrying a chain, a fader and an automation clock for several tracks at once (`<hf-audio-group>`). Don't use for sourcing or generating audio — finding BGM, SFX, or making a voiceover is `/media-use`. Don't use for clip timing or track layout, which is `/hyperframes-core`.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | ffmpeg, hyperframes, node |
| Processo (cabeçalhos) | HyperFrames Audio → How it fits together → First, work out what is wrong → Start from the symptom → Reach for a family by the problem, not the name → Voiceover carve → One bus for many tracks → Automation → Verify |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 25,400 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/carve.mjs`
- `scripts/carve.test.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
