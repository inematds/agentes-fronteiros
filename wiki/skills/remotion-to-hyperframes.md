---
type: Skill
title: remotion-to-hyperframes
description: Port an existing Remotion (React) composition's source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — one-way, Remotion-only. A passing
  Remotion mention, reference…
resource: file:///home/nmaldaner/.claude/skills/remotion-to-hyperframes/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/remotion-to-hyperframes/SKILL.md
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
  arquivos: 70
  subpastas:
  - assets
  - references
  - scripts
  scripts:
  - assets/test-corpus/run.sh
  - assets/test-corpus/tier-1-title-card/remotion-src/remotion.config.ts
  - assets/test-corpus/tier-1-title-card/remotion-src/src/index.ts
  - assets/test-corpus/tier-2-multi-scene/remotion-src/remotion.config.ts
  - assets/test-corpus/tier-2-multi-scene/remotion-src/src/index.ts
  - assets/test-corpus/tier-2-multi-scene/setup.sh
  - assets/test-corpus/tier-3-data-driven/remotion-src/remotion.config.ts
  - assets/test-corpus/tier-3-data-driven/remotion-src/src/index.ts
  - assets/test-corpus/tier-4-escape-hatch/validate.sh
  - scripts/frame_strip.sh
  - scripts/lint_source.py
  - scripts/render_diff.sh
  - scripts/tests/smoke.sh
  ferramentas:
  - github
  - heygen
  - hyperframes
  - remotion
  gatilhos:
  - make something like my Remotion video
  tamanho_skill_md: 10619
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# remotion-to-hyperframes

## Descrição (do SKILL.md)

Port an existing Remotion (React) composition's source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — one-way, Remotion-only. A passing Remotion mention, reference-only code, or "make something like my Remotion video" is a fresh build (/general-video). Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Port an existing Remotion (React) composition's source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — o… |
| Entradas (gatilhos) | make something like my Remotion video |
| Ferramentas citadas | github, heygen, hyperframes, remotion |
| Processo (cabeçalhos) | Remotion to HyperFrames → Overview → When to use → Workflow → Step 1: Lint the source → Step 2: Plan the translation → Step 3: Generate the HF composition → Step 4: Validate → Render Remotion baseline (after npm install in the fixture) → Render HF translation |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references, scripts · SKILL.md com 10,619 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/test-corpus/run.sh`
- `assets/test-corpus/tier-1-title-card/remotion-src/remotion.config.ts`
- `assets/test-corpus/tier-1-title-card/remotion-src/src/index.ts`
- `assets/test-corpus/tier-2-multi-scene/remotion-src/remotion.config.ts`
- `assets/test-corpus/tier-2-multi-scene/remotion-src/src/index.ts`
- `assets/test-corpus/tier-2-multi-scene/setup.sh`
- `assets/test-corpus/tier-3-data-driven/remotion-src/remotion.config.ts`
- `assets/test-corpus/tier-3-data-driven/remotion-src/src/index.ts`
- `assets/test-corpus/tier-4-escape-hatch/validate.sh`
- `scripts/frame_strip.sh`
- `scripts/lint_source.py`
- `scripts/render_diff.sh`
- `scripts/tests/smoke.sh`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
