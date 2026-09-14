---
type: Skill
title: anuncio-edita
description: ''
resource: file:///home/nmaldaner/.claude/skills/anuncio-edita/SKILL.md
tags:
- skill
- publicacao
sources:
- path: /home/nmaldaner/.claude/skills/anuncio-edita/SKILL.md
  author: human:nei
  last_modified: '2026-09-06'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/publicacao
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 12
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/captions.py
  - scripts/export-srt.py
  - scripts/jargon-fix.py
  - scripts/master-audio.py
  - scripts/overlay-fallback/build_track.py
  - scripts/overlay-fallback/compose.py
  - scripts/overlay-fallback/compute_marks.py
  - scripts/overlay-fallback/make_bed.py
  - scripts/overlay-fallback/render_overlays.py
  ferramentas:
  - chatterbox
  - ffmpeg
  - inemavox
  - python
  - whisper
  gatilhos: []
  tamanho_skill_md: 10169
migracao:
  estagio: inventariado
  cluster: publicacao
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# anuncio-edita

## Descrição (do SKILL.md)

_sem descrição_

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | — |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | chatterbox, ffmpeg, inemavox, python, whisper |
| Processo (cabeçalhos) | /anuncio-edita — Pós-produção de anúncios gerados com IA → A doutrina, antes do pipeline → Ferramentas (uma só fonte de verdade) → F0 · Ingestão e diagnóstico → F1 · Montagem (só se chegam módulos soltos) → F2 · Pista de voz → F3 · Legendas (sempre, e sóbrias) → 1. Transcript word-level do master de áudio + correção de jargão → 2. Páginas sóbrias → 3. Queimar: via libass (ass=) ou via overlay-fallback (ver README dele) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 10,169 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/captions.py`
- `scripts/export-srt.py`
- `scripts/jargon-fix.py`
- `scripts/master-audio.py`
- `scripts/overlay-fallback/build_track.py`
- `scripts/overlay-fallback/compose.py`
- `scripts/overlay-fallback/compute_marks.py`
- `scripts/overlay-fallback/make_bed.py`
- `scripts/overlay-fallback/render_overlays.py`

## Cluster

[publicacao](../clusters/publicacao.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
