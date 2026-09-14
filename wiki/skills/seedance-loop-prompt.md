---
type: Skill
title: seedance-loop-prompt
description: Use when generating a Seedance 2 video prompt for a seamless looping background video. Trigger when the user describes a product, scene, or concept for a website background loop, mentions Seedance,
  asks for a looping vi…
resource: file:///home/nmaldaner/.claude/skills/seedance-loop-prompt/SKILL.md
tags:
- skill
- video-ia
sources:
- path: /home/nmaldaner/.claude/skills/seedance-loop-prompt/SKILL.md
  author: human:nei
  last_modified: '2026-04-10'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-ia
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - references
  scripts: []
  ferramentas:
  - seedance
  gatilhos:
  - loop video
  - website background video
  - product loop
  - endless loop video
  tamanho_skill_md: 8772
migracao:
  estagio: inventariado
  cluster: video-ia
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# seedance-loop-prompt

## Descrição (do SKILL.md)

Use when generating a Seedance 2 video prompt for a seamless looping background video. Trigger when the user describes a product, scene, or concept for a website background loop, mentions Seedance, asks for a looping video prompt, background video, or provides a product with headlines for a cinematic background. Also trigger on phrases like "loop video", "website background video", "product loop", "endless loop video", or any visual concept intended for continuous playback on a webpage.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Use when generating a Seedance 2 video prompt for a seamless looping background video. Trigger when the user describes a product, scene, or concept for a websi… |
| Entradas (gatilhos) | loop video, website background video, product loop, endless loop video |
| Ferramentas citadas | seedance |
| Processo (cabeçalhos) | Seedance Loop Prompt Builder → Input expectations → Confidence gate → Direction inference → Output format → SCENE → CAMERA → ACTION ARC → TEXT CHOREOGRAPHY → LIGHTING & ATMOSPHERE |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 8,772 chars |

## Cluster

[video-ia](../clusters/video-ia.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
