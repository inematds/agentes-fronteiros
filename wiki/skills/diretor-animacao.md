---
type: Skill
title: diretor-animacao
description: O Diretor de Animação — transforma IMAGENS PRONTAS (fotos reais e/ou ilustrações) + NARRAÇÃO em um FILME profissional, sem IA generativa de vídeo. Analisa cada imagem (visão), segmenta a narração
  em beats, e decide POR…
resource: file:///home/nmaldaner/.claude/skills/diretor-animacao/SKILL.md
tags:
- skill
- pixflow
sources:
- path: /home/nmaldaner/.claude/skills/diretor-animacao/SKILL.md
  author: human:nei
  last_modified: '2026-06-10'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pixflow
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 3
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/montar-trilha.mjs
  ferramentas:
  - flux
  - hyperframes
  - node
  - pixflow
  - tts
  gatilhos:
  - vira filme
  - anima essas imagens
  - dirige esse material
  - filme com essas fotos
  - motion film das imagens
  tamanho_skill_md: 3392
migracao:
  estagio: inventariado
  cluster: pixflow
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# diretor-animacao

## Descrição (do SKILL.md)

O Diretor de Animação — transforma IMAGENS PRONTAS (fotos reais e/ou ilustrações) + NARRAÇÃO em um FILME profissional, sem IA generativa de vídeo. Analisa cada imagem (visão), segmenta a narração em beats, e decide POR imagem a câmera (18 movimentos + framing from/to), duração, transição, look e parallax, seguindo gramática cinematográfica. Render via pixflow (motor v2.3). Use quando o usuário der um conjunto de imagens + narração (áudio ou texto) e pedir "vira filme", "anima essas imagens", "dirige esse material", "filme com essas fotos", "motion film das imagens".

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | O Diretor de Animação — transforma IMAGENS PRONTAS (fotos reais e/ou ilustrações) + NARRAÇÃO em um FILME profissional, sem IA generativa de vídeo. Analisa cada… |
| Entradas (gatilhos) | vira filme, anima essas imagens, dirige esse material, filme com essas fotos, motion film das imagens |
| Ferramentas citadas | flux, hyperframes, node, pixflow, tts |
| Processo (cabeçalhos) | Diretor de Animação → Motor → Fluxo (sempre nesta ordem) → Regras de ouro → Referências |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 3,392 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/montar-trilha.mjs`

## Cluster

[pixflow](../clusters/pixflow.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
