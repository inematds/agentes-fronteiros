---
type: Skill
title: comfy-director
description: Use when asked to make a narrative video — an ad, brand film, short, trailer, music video, or any multi-shot clip that tells a story (not a single shot or loop). Also use when a video was rejected
  for "no story", "doesn…
resource: file:///home/nmaldaner/.claude/skills/comfy-director/SKILL.md
tags:
- skill
- comfy
sources:
- path: /home/nmaldaner/.claude/skills/comfy-director/SKILL.md
  author: human:nei
  last_modified: '2026-09-02'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/comfy
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - ffmpeg
  - kling
  - tts
  gatilhos:
  - no story
  - doesn't flow
  - feels like a montage
  tamanho_skill_md: 6885
migracao:
  estagio: inventariado
  cluster: comfy
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# comfy-director

## Descrição (do SKILL.md)

Use when asked to make a narrative video — an ad, brand film, short, trailer, music video, or any multi-shot clip that tells a story (not a single shot or loop). Also use when a video was rejected for "no story", "doesn't flow", "feels like a montage", or characters that change between shots.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Use when asked to make a narrative video — an ad, brand film, short, trailer, music video, or any multi-shot clip that tells a story (not a single shot or loop… |
| Entradas (gatilhos) | no story, doesn't flow, feels like a montage |
| Ferramentas citadas | ffmpeg, kling, tts |
| Processo (cabeçalhos) | Comfy Director → Order of operations → Screenplay rules → Concept rules → Prompting shots → Continuity toolkit → Audio → Production ops → Common mistakes (each killed a real cut) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 6,885 chars |

## Cluster

[comfy](../clusters/comfy.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
