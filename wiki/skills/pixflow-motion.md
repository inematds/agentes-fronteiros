---
type: Skill
title: pixflow-motion
description: 'Imagens estáticas viram filme cinematográfico — parallax 2.5D real, movimentos de câmera e grain/LUT/bloom — em código aberto, SEM gerador de vídeo por IA. Gatilho: "dar movimento a uma foto",
  "vídeo determinístico/sem…'
resource: file:///home/nmaldaner/.claude/skills/pixflow-motion/SKILL.md
tags:
- skill
- pixflow
sources:
- path: /home/nmaldaner/.claude/skills/pixflow-motion/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pixflow
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 11110
  subpastas:
  - cli
  - node_modules
  - public
  - src
  scripts:
  - cli/depth.mjs
  - cli/genimg.mjs
  - cli/make-test-image.mjs
  - cli/pixflow-motion.mjs
  - src/camera.js
  - src/layout.js
  - src/looks.js
  - src/shaders.js
  ferramentas:
  - ffmpeg
  - flux
  - kling
  - node
  - pixflow
  - playwright
  - remotion
  gatilhos:
  - dar movimento a uma foto
  - vídeo determinístico/sem IA
  tamanho_skill_md: 3743
migracao:
  estagio: inventariado
  cluster: pixflow
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# pixflow-motion

## Descrição (do SKILL.md)

Imagens estáticas viram filme cinematográfico — parallax 2.5D real, movimentos de câmera e grain/LUT/bloom — em código aberto, SEM gerador de vídeo por IA. Gatilho: "dar movimento a uma foto", "vídeo determinístico/sem IA". Consome um movie spec YAML.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Imagens estáticas viram filme cinematográfico — parallax 2.5D real, movimentos de câmera e grain/LUT/bloom — em código aberto, SEM gerador de vídeo por IA. Gat… |
| Entradas (gatilhos) | dar movimento a uma foto, vídeo determinístico/sem IA |
| Ferramentas citadas | ffmpeg, flux, kling, node, pixflow, playwright, remotion |
| Processo (cabeçalhos) | pixflow-motion → Quando usar → Pré-requisitos (uma vez) → Fluxo de uso → Comandos → Movie spec (resumo) → Arquitetura → Estado (MVP) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: cli, node_modules, public, src · SKILL.md com 3,743 chars |

## Scripts (candidatos a `agent/tools/`)

- `cli/depth.mjs`
- `cli/genimg.mjs`
- `cli/make-test-image.mjs`
- `cli/pixflow-motion.mjs`
- `src/camera.js`
- `src/layout.js`
- `src/looks.js`
- `src/shaders.js`

## Cluster

[pixflow](../clusters/pixflow.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
