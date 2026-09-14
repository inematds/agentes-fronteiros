---
type: Skill
title: hyperframes-animation
description: All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default,
  plus Lottie, Three.js, Anim…
resource: file:///home/nmaldaner/.claude/skills/hyperframes-animation/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/hyperframes-animation/SKILL.md
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
  arquivos: 121
  subpastas:
  - adapters
  - blueprints
  - examples
  - rules
  - scripts
  - transitions
  scripts:
  - scripts/animation-map-sampling.mjs
  - scripts/animation-map-sampling.test.mjs
  - scripts/animation-map.mjs
  - scripts/animation-map.test.mjs
  - scripts/package-loader.mjs
  - scripts/package-loader.test.mjs
  ferramentas:
  - hyperframes
  - node
  gatilhos: []
  tamanho_skill_md: 7755
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# hyperframes-animation

## Descrição (do SKILL.md)

All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP eases / Lottie player / Three.js mixer). Also covers auditing an existing composition's choreography (animation map) and 24 named text-animation effects. HyperFrames-native: single paused timeline, seek-safe, deterministic.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | hyperframes, node |
| Processo (cabeçalhos) | HyperFrames Animation → Default: compose atomic rules → Load a blueprint when → Routing → Picking a runtime → Critical Constraints → Scripts → See Also |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: adapters, blueprints, examples, rules, scripts, transitions · SKILL.md com 7,755 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/animation-map-sampling.mjs`
- `scripts/animation-map-sampling.test.mjs`
- `scripts/animation-map.mjs`
- `scripts/animation-map.test.mjs`
- `scripts/package-loader.mjs`
- `scripts/package-loader.test.mjs`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
