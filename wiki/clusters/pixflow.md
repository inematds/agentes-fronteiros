---
type: Cluster
title: Pixflow (imagens → filme sem IA de vídeo)
description: 5 skills disputam a intenção “Pixflow (imagens → filme sem IA de vídeo)”.
tags:
- cluster
- pixflow
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/diretor-animacao
- skills/filme
- skills/pixflow-motion
- skills/pixflow-trailer
- skills/videoanima
cluster:
  id: pixflow
  membros:
  - diretor-animacao
  - filme
  - pixflow-motion
  - pixflow-trailer
  - videoanima
---

# Cluster: Pixflow (imagens → filme sem IA de vídeo)

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [diretor-animacao](../skills/diretor-animacao.md) | O Diretor de Animação — transforma IMAGENS PRONTAS (fotos reais e/ou ilustrações) + NARRAÇÃO em um FILME prof… | 1 | flux, hyperframes, node, pixflow, tts |
| [filme](../skills/filme.md) | historia.json (do skill roteiro) vira FILME narrado em parallax 2.5D no pixflow — camera por emocao, musica e… | 9 | ffmpeg, flux, inemavox, node, pixflow |
| [pixflow-motion](../skills/pixflow-motion.md) | Imagens estáticas viram filme cinematográfico — parallax 2.5D real, movimentos de câmera e grain/LUT/bloom —… | 8 | ffmpeg, flux, kling, node, pixflow |
| [pixflow-trailer](../skills/pixflow-trailer.md) | Decupagem (lista de shots com câmera e mood) vira TRAILER narrado com música e SFX, sem IA de vídeo. Gera as… | 9 | ffmpeg, flux, inemavox, node, pixflow |
| [videoanima](../skills/videoanima.md) | História → filme animado vertical COM DIREÇÃO: escreve a decupagem plano a plano, mostra o custo, e só então… | 0 | chatterbox, ffmpeg, flux, inemavox, kling |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`flux` (5×), `node` (4×), `pixflow` (4×), `ffmpeg` (4×), `tts` (3×), `inemavox` (3×), `python` (2×), `kling` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
