---
type: Skill
title: embedded-captions
description: Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded behind the subject, VFX
  captions, “炸/特效/酷炫字幕,” or a na…
resource: file:///home/nmaldaner/.claude/skills/embedded-captions/SKILL.md
tags:
- skill
- hyperframes
sources:
- path: /home/nmaldaner/.claude/skills/embedded-captions/SKILL.md
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
  arquivos: 142
  subpastas:
  - assets
  - dna
  - modes
  - references
  - scripts
  - themes
  scripts:
  - scripts/gen-stroke-path.py
  - scripts/make-theme.test.mjs
  - scripts/prepare.sh
  - scripts/preview-frames.test.mjs
  - scripts/render-and-composite.sh
  - scripts/render-theme.sh
  ferramentas:
  - ffmpeg
  - github
  - hyperframes
  - node
  - python
  - whisper
  gatilhos:
  - 炸/特效/酷炫字幕,
  tamanho_skill_md: 32733
migracao:
  estagio: inventariado
  cluster: hyperframes
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# embedded-captions

## Descrição (do SKILL.md)

Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded behind the subject, VFX captions, “炸/特效/酷炫字幕,” or a named identity from the 35-style catalog. Route by visual identity, not by backend engine. The quiet `anchor` rail is the default; embed every word only when the user explicitly wants a fully cinematic treatment. The workflow runs locally end to end, including transcription and subject matting; split multi-shot footage before applying it.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions emb… |
| Entradas (gatilhos) | 炸/特效/酷炫字幕, |
| Ferramentas citadas | ffmpeg, github, hyperframes, node, python, whisper |
| Processo (cabeçalhos) | Embedded Captions → Operational flow (TL;DR) → Caption model — rail + embed → Step 0 — pick ONE identity from the CATALOG → Decision gate — RUN FIRST → Pre-flight probes (cost nothing, prevent the worst failures) → Pipeline — 5 steps → Step 3 — Cinematic mode (pure embed) → Step 3 — Theme mode (themed constitution) → Visual QA — preview BEFORE you render |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, dna, modes, references, scripts, themes · SKILL.md com 32,733 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/gen-stroke-path.py`
- `scripts/make-theme.test.mjs`
- `scripts/prepare.sh`
- `scripts/preview-frames.test.mjs`
- `scripts/render-and-composite.sh`
- `scripts/render-theme.sh`

## Cluster

[hyperframes](../clusters/hyperframes.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
