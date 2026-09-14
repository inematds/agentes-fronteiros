---
type: Skill
title: slideshow
description: Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker
  notes; also converts an ex…
resource: file:///home/nmaldaner/.claude/skills/slideshow/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/slideshow/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/hyperframes
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - references
  scripts: []
  ferramentas:
  - hyperframes
  - mcp
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 33631
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# slideshow

## Descrição (do SKILL.md)

Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an existing page into a deck. Output is a navigable deck, not a rendered MP4. If the user didn't explicitly ask for a slideshow, confirm before authoring. Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and bui… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | hyperframes, mcp, node, tts |
| Processo (cabeçalhos) | Slideshow authoring contract → Output — a navigable deck, not a linear MP4 → Intent confirmation → The two pieces → 1. Scenes — declared the normal way → 2. The JSON island — one script block per composition → Schema → `SlideshowManifest` (the top-level island object) → `SlideRef` → `SlideHotspot` |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 33,631 chars |

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
