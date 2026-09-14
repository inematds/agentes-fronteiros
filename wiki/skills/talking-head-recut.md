---
type: Skill
title: talking-head-recut
description: Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture
  — synced to the transcript,…
resource: file:///home/nmaldaner/.claude/skills/talking-head-recut/SKILL.md
tags:
- skill
- reels
sources:
- path: /home/nmaldaner/.claude/skills/talking-head-recut/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/reels
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 28
  subpastas:
  - assets
  - references
  scripts:
  - assets/vendor/gsap.min.js
  - media-contract.test.mjs
  ferramentas:
  - ffmpeg
  - hyperframes
  - whisper
  gatilhos:
  - graphic overlays
  - on-screen graphics
  - package / dress up my video
  tamanho_skill_md: 65360
migracao:
  estagio: inventariado
  cluster: reels
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# talking-head-recut

## Descrição (do SKILL.md)

Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript, on a 16:9 / 9:16 / 4:5 canvas of your choice; the clip plays untouched underneath. Trigger on "graphic overlays", "on-screen graphics", "package / dress up my video". Not plain subtitles (/embedded-captions). Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes,… |
| Entradas (gatilhos) | graphic overlays, on-screen graphics, package / dress up my video |
| Ferramentas citadas | ffmpeg, hyperframes, whisper |
| Processo (cabeçalhos) | Talking Head Recut → CLI Resolution → hyperframes — transcription (local Whisper) + rendering the assembled HTML to MP4 → Workflow → 1. Check Environment → confirm bundled assets: → 2. Create a Work Directory → 3. Extract Audio and Metadata → metadata — duration / width / height / fps → audio |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 65,360 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/vendor/gsap.min.js`
- `media-contract.test.mjs`

## Cluster

[reels](../clusters/reels.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
