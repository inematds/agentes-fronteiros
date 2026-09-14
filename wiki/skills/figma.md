---
type: Skill
title: figma
description: Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not slides) (REST/CLI), connector-assisted
  motion when…
resource: file:///home/nmaldaner/.claude/skills/figma/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/figma/SKILL.md
  author: human:nei
  last_modified: '2026-08-29'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - scripts
  scripts:
  - scripts/verify-motion.mjs
  ferramentas:
  - hyperframes
  - node
  gatilhos: []
  tamanho_skill_md: 17829
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# figma

## Descrição (do SKILL.md)

Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not slides) (REST/CLI), connector-assisted motion when available, and shaders from a connector or native export. Use when the user pastes a figma.com link or asks to bring a Figma design, frame, logo, brand, or animation into a video/composition.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as sta… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | hyperframes, node |
| Processo (cabeçalhos) | Figma → HyperFrames → Auth — two credentials, scoped → Routing → Assets (Phase 1 — CLI) → Tokens (Phase 2 — CLI) → Components (Phase 3 — CLI) → Motion (Phase 4 — connector-assisted) → Shaders (Phase 5 — mostly manual) → Storyboards (a SECTION of scene frames → animation) → Determinism |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 17,829 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/verify-motion.mjs`

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
