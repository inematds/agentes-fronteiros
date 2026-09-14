---
type: Cluster
title: Séries / HQ / referências de personagem
description: 4 skills disputam a intenção “Séries / HQ / referências de personagem”.
tags:
- cluster
- inemaref
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/inemaref-folder
- skills/inemaref-motioncomic
- skills/inemaref-quadrinho
- skills/inemaref-serie
cluster:
  id: inemaref
  membros:
  - inemaref-folder
  - inemaref-motioncomic
  - inemaref-quadrinho
  - inemaref-serie
---

# Cluster: Séries / HQ / referências de personagem

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [inemaref-folder](../skills/inemaref-folder.md) | Cria a FICHA DE REFERENCIA (model sheet) de um personagem a partir de uma FOTO (pessoa real) ou de um TEXTO (… | 18 | flux, python |
| [inemaref-motioncomic](../skills/inemaref-motioncomic.md) | Transforma uma HISTORIA em quadros num VIDEO de motion comic (16:9) — a camera da ZOOM em cada quadro durante… | 17 | ffmpeg, flux, inemavox, pixflow, python |
| [inemaref-quadrinho](../skills/inemaref-quadrinho.md) | Monta uma PAGINA de quadrinho/manga a partir de uma HISTORIA (e, opcionalmente, da referencia.json de um pers… | 7 | flux, python |
| [inemaref-serie](../skills/inemaref-serie.md) | Cria uma SERIE completa a partir de um ASSUNTO — escreve a BIBLIA (premissa, protagonista com folder, elenco,… | 23 | ffmpeg, inemavox, pixflow, python, tts |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`python` (4×), `flux` (3×), `ffmpeg` (2×), `inemavox` (2×), `pixflow` (2×), `tts` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
