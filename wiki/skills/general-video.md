---
type: Skill
title: general-video
description: 'Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and sizzle reels, montages,
  static loops, static titl…'
resource: file:///home/nmaldaner/.claude/skills/general-video/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/general-video/SKILL.md
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
  arquivos: 4
  subpastas:
  - scripts
  - sub-agents
  scripts:
  - scripts/frame-packets.mjs
  - scripts/frame-packets.test.mjs
  ferramentas:
  - hyperframes
  - node
  gatilhos: []
  tamanho_skill_md: 20760
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# general-video

## Descrição (do SKILL.md)

Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and sizzle reels, montages, static loops, static title cards, footage remixes, and freeform builds. Use motion-graphics instead for a short unnarrated motion-first unit, including an animated title. Route fresh creation through hyperframes before using this skill.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces,… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | hyperframes, node |
| Processo (cabeçalhos) | General video → 1. Apply cross-cutting source adapters → 2. Start from project state → 3. Interpret the run shape → Companion flow → 4. Load required knowledge before each stage → 5. Execute the composition → 6. Gates that always apply → Keep scope exact → Establish design before HTML |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts, sub-agents · SKILL.md com 20,760 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/frame-packets.mjs`
- `scripts/frame-packets.test.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
