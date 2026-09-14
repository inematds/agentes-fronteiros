---
type: Skill
title: ugc-seedance25
description: Anúncio UGC (creator falando pro celular, one-take 30 s, 9:16, 1080p) com Seedance 2.5 — brief do produto vira 3 prompts prontos (produto, creator, vídeo) na receita do pack "Seedance 2.5 UGC
  Ads", adaptada pra Magnific…
resource: file:///home/nmaldaner/.claude/skills/ugc-seedance25/SKILL.md
tags:
- skill
- video-ia
sources:
- path: /home/nmaldaner/.claude/skills/ugc-seedance25/SKILL.md
  author: human:nei
  last_modified: '2026-09-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-ia
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 5
  subpastas:
  - references
  scripts: []
  ferramentas:
  - chatterbox
  - ffmpeg
  - flux
  - inemavox
  - magnific
  - seedance
  gatilhos:
  - Seedance 2.5 UGC Ads
  - anúncio ugc
  - ugc ad
  - ad estilo creator
  - vídeo de produto falando pro celular
  - seedance ugc
  tamanho_skill_md: 5359
migracao:
  estagio: inventariado
  cluster: video-ia
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# ugc-seedance25

## Descrição (do SKILL.md)

Anúncio UGC (creator falando pro celular, one-take 30 s, 9:16, 1080p) com Seedance 2.5 — brief do produto vira 3 prompts prontos (produto, creator, vídeo) na receita do pack "Seedance 2.5 UGC Ads", adaptada pra Magnific MCP. Gera o brief.md sempre; executa na Magnific só se pedido, com gate de custo, rascunho 720p e QA em frames. Gatilho: "anúncio ugc", "ugc ad", "ad estilo creator", "vídeo de produto falando pro celular", "seedance ugc".

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Anúncio UGC (creator falando pro celular, one-take 30 s, 9:16, 1080p) com Seedance 2.5 — brief do produto vira 3 prompts prontos (produto, creator, vídeo) na r… |
| Entradas (gatilhos) | Seedance 2.5 UGC Ads, anúncio ugc, ugc ad, ad estilo creator, vídeo de produto falando pro celular, seedance ugc |
| Ferramentas citadas | chatterbox, ffmpeg, flux, inemavox, magnific, seedance |
| Processo (cabeçalhos) | /ugc-seedance25 — anúncio UGC one-take com Seedance 2.5 → 1 · Brief (uma rodada de perguntas, em texto livre) → 2 · Escrever os 3 prompts → 3 · Entregar o brief (sempre) → 4 · Executar na Magnific (só se pedido) → 5 · QA em frames (sempre que houver um vídeo) → contact sheet 3x3 (um frame a cada ~3,3 s de um vídeo de 30 s) → rótulo espelhado? corrige o clipe inteiro → O que não fazer |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 5,359 chars |

## Cluster

[video-ia](../clusters/video-ia.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
