---
type: Skill
title: pr-to-video
description: Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor walkthrough built from
  the diff, commits, and file…
resource: file:///home/nmaldaner/.claude/skills/pr-to-video/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/pr-to-video/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-explicativo
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 30
  subpastas:
  - references
  - scripts
  - sub-agents
  scripts:
  - scripts/assemble-index.mjs
  - scripts/assemble-index.test.mjs
  - scripts/audio.mjs
  - scripts/build-frame.mjs
  - scripts/captions.mjs
  - scripts/captions.test.mjs
  - scripts/fetch-people-avatars.mjs
  - scripts/fetch-pr.mjs
  - scripts/frame-contract.test.mjs
  - scripts/frame-packets.mjs
  - scripts/ingest.mjs
  - scripts/lib/assets.mjs
  - scripts/lib/dimensions.mjs
  - scripts/lib/frame-contract.mjs
  - scripts/lib/pad-frame-duration.mjs
  - scripts/lib/storyboard.mjs
  - scripts/lib/tokens.mjs
  - scripts/lib/transition-registry.mjs
  - scripts/preflight.mjs
  - scripts/project-dir.mjs
  - scripts/transitions.mjs
  - scripts/workflow-guardrails.test.mjs
  ferramentas:
  - github
  - heygen
  - hyperframes
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 32655
migracao:
  estagio: inventariado
  cluster: video-explicativo
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# pr-to-video

## Descrição (do SKILL.md)

Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files: the input is a code change, not a website. Not a product promo (/product-launch-video) or a no-PR topic explainer (/faceless-explainer). Unclear → /hyperframes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, heygen, hyperframes, node, tts |
| Processo (cabeçalhos) | PR to HyperFrames → Step 0: Setup → Step 1: Ingest the PR (no capture) → Fetch the PR deterministically: runs gh, completes the files list via paginated → gh api (so a big PR doesn't truncate at ~100 files), writes only capture/pr.json + → capture/diff.patch — no scratch dir. gh auth / not-found / private errors exit 1 here. → Offline transform → capture/extracted/{tokens.json (colors:[] → code-editorial palette), → visible-text.txt (the brief), people.json (contributors, bot-filtered, name+login, → avatarFile=assets/<login>.png)}. → The people front's one network step — download each contributor's GitHub avatar to |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts, sub-agents · SKILL.md com 32,655 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/assemble-index.mjs`
- `scripts/assemble-index.test.mjs`
- `scripts/audio.mjs`
- `scripts/build-frame.mjs`
- `scripts/captions.mjs`
- `scripts/captions.test.mjs`
- `scripts/fetch-people-avatars.mjs`
- `scripts/fetch-pr.mjs`
- `scripts/frame-contract.test.mjs`
- `scripts/frame-packets.mjs`
- `scripts/ingest.mjs`
- `scripts/lib/assets.mjs`
- `scripts/lib/dimensions.mjs`
- `scripts/lib/frame-contract.mjs`
- `scripts/lib/pad-frame-duration.mjs`
- `scripts/lib/storyboard.mjs`
- `scripts/lib/tokens.mjs`
- `scripts/lib/transition-registry.mjs`
- `scripts/preflight.mjs`
- `scripts/project-dir.mjs`
- `scripts/transitions.mjs`
- `scripts/workflow-guardrails.test.mjs`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
