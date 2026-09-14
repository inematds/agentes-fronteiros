---
type: Cluster
title: Vídeo explicativo / narrado
description: 6 skills disputam a intenção “Vídeo explicativo / narrado”.
tags:
- cluster
- video-explicativo
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/faceless-explainer
- skills/pr-to-video
- skills/product-launch-video
- skills/video-demonstrativo
- skills/video-explicativo
- skills/videoprodutor
cluster:
  id: video-explicativo
  membros:
  - faceless-explainer
  - pr-to-video
  - product-launch-video
  - video-demonstrativo
  - video-explicativo
  - videoprodutor
---

# Cluster: Vídeo explicativo / narrado

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [faceless-explainer](../skills/faceless-explainer.md) | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site… | 17 | github, heygen, hyperframes, node, tts |
| [pr-to-video](../skills/pr-to-video.md) | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change ex… | 22 | github, heygen, hyperframes, node, tts |
| [product-launch-video](../skills/product-launch-video.md) | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, f… | 23 | gemini, github, heygen, hyperframes, mcp |
| [video-demonstrativo](../skills/video-demonstrativo.md) | Walkthrough narrado de uma aplicação web a partir do link: navega o app de verdade, captura as telas reais e… | 4 | agent-browser, ffmpeg, flux, hyperframes, node |
| [video-explicativo](../skills/video-explicativo.md) | Cria vídeos explicativos completos em PT-BR (HTML→MP4 via HyperFrames) a partir de um assunto — roteiro, narr… | 3 | chatterbox, ffmpeg, flux, github, heygen |
| [videoprodutor](../skills/videoprodutor.md) | O Produtor — orquestra link/assunto → vídeo profissional ponta a ponta (plano, direção, imagem/SVG, voz, rend… | 4 | ffmpeg, flux, hyperframes, node, python |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`hyperframes` (6×), `node` (6×), `tts` (6×), `github` (4×), `heygen` (4×), `ffmpeg` (3×), `flux` (3×), `python` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
