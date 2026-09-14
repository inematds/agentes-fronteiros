---
type: Cluster
title: Reels / vídeo curto vertical
description: 5 skills disputam a intenção “Reels / vídeo curto vertical”.
tags:
- cluster
- reels
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/forja-reel
- skills/reel-edita-inema
- skills/reel-edita-inematds
- skills/roteirista-inema
- skills/talking-head-recut
cluster:
  id: reels
  membros:
  - forja-reel
  - reel-edita-inema
  - reel-edita-inematds
  - roteirista-inema
  - talking-head-recut
---

# Cluster: Reels / vídeo curto vertical

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [forja-reel](../skills/forja-reel.md) | META-SKILL: entrevista você sobre estilo e identidade e gera A SUA própria skill "/reel-edita", com motor de… | 8 | ffmpeg, flux, groq, hyperframes, node |
| [reel-edita-inema](../skills/reel-edita-inema.md) | Monta o REEL EMPILHADO da marca INEMA (9:16) a partir de vídeos 16:9 — topo impactante, avatar no meio, expli… | 17 | ffmpeg, flux, groq, heygen, hyperframes |
| [reel-edita-inematds](../skills/reel-edita-inematds.md) | Converte um vídeo bruto vertical num reel/TikTok produzido com o estilo de INEMATDS — corta repetições/silênc… | 7 | ffmpeg, groq, hyperframes, python, telegram |
| [roteirista-inema](../skills/roteirista-inema.md) | Transforma qualquer ideia bruta do Nei em roteiro de Reels/Shorts pronto para gravar, seguindo o método INEMA… | 0 |  |
| [talking-head-recut](../skills/talking-head-recut.md) | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kin… | 2 | ffmpeg, hyperframes, whisper |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`ffmpeg` (4×), `hyperframes` (4×), `whisper` (4×), `groq` (3×), `python` (3×), `flux` (2×), `telegram` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
