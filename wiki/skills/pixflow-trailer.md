---
type: Skill
title: pixflow-trailer
description: Decupagem (lista de shots com câmera e mood) vira TRAILER narrado com música e SFX, sem IA de vídeo. Gera as imagens, mapeia cada shot para os primitivos de câmera e renderiza. Constrói por
  cima de pixflow-motion.
resource: file:///home/nmaldaner/.claude/skills/pixflow-trailer/SKILL.md
tags:
- skill
- pixflow
sources:
- path: /home/nmaldaner/.claude/skills/pixflow-trailer/SKILL.md
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
  arquivos: 14
  subpastas:
  - examples
  - templates
  scripts:
  - examples/avatar-fogo-cinzas/build.mjs
  - examples/avatar-fogo-cinzas/gen-audio.mjs
  - examples/avatar-fogo-cinzas/gen-narracao.mjs
  - examples/dragao-chama-do-saber/build.mjs
  - examples/dragao-chama-do-saber/gen-audio.mjs
  - examples/dragao-chama-do-saber/gen-narracao.mjs
  - templates/build.template.mjs
  - templates/gen-audio.mjs
  - templates/gen-narracao.mjs
  ferramentas:
  - ffmpeg
  - flux
  - inemavox
  - node
  - pixflow
  - tts
  gatilhos: []
  tamanho_skill_md: 5288
migracao:
  estagio: inventariado
  cluster: pixflow
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# pixflow-trailer

## Descrição (do SKILL.md)

Decupagem (lista de shots com câmera e mood) vira TRAILER narrado com música e SFX, sem IA de vídeo. Gera as imagens, mapeia cada shot para os primitivos de câmera e renderiza. Constrói por cima de pixflow-motion.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Decupagem (lista de shots com câmera e mood) vira TRAILER narrado com música e SFX, sem IA de vídeo. Gera as imagens, mapeia cada shot para os primitivos de câ… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | ffmpeg, flux, inemavox, node, pixflow, tts |
| Processo (cabeçalhos) | pixflow-trailer → Quando usar → Pré-requisitos → Fluxo (o que fazer) → Princípio de eficiência → Limites herdados do motor (citar ao usuário quando relevante) → Exemplo completo |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: examples, templates · SKILL.md com 5,288 chars |

## Scripts (candidatos a `agent/tools/`)

- `examples/avatar-fogo-cinzas/build.mjs`
- `examples/avatar-fogo-cinzas/gen-audio.mjs`
- `examples/avatar-fogo-cinzas/gen-narracao.mjs`
- `examples/dragao-chama-do-saber/build.mjs`
- `examples/dragao-chama-do-saber/gen-audio.mjs`
- `examples/dragao-chama-do-saber/gen-narracao.mjs`
- `templates/build.template.mjs`
- `templates/gen-audio.mjs`
- `templates/gen-narracao.mjs`

## Cluster

[pixflow](../clusters/pixflow.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
