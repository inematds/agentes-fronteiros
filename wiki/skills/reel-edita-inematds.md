---
type: Skill
title: reel-edita-inematds
description: Converte um vídeo bruto vertical num reel/TikTok produzido com o estilo de INEMATDS — corta repetições/silêncios/erros, propõe um tratamento adaptado ao conteúdo, monta câmera alternando entre
  PiP/tela-dividida + B-roll…
resource: file:///home/nmaldaner/.claude/skills/reel-edita-inematds/SKILL.md
tags:
- skill
- reels
sources:
- path: /home/nmaldaner/.claude/skills/reel-edita-inematds/SKILL.md
  author: human:nei
  last_modified: '2026-07-18'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/reels
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 21
  subpastas:
  - assets
  - references
  - scripts
  scripts:
  - scripts/captions.py
  - scripts/cut.py
  - scripts/islands.py
  - scripts/lint-timeline.py
  - scripts/make-sfx.sh
  - scripts/mix-sfx.py
  - scripts/verify-cut.py
  ferramentas:
  - ffmpeg
  - groq
  - hyperframes
  - python
  - telegram
  - whisper
  gatilhos:
  - edita este vídeo para reel
  - faz o reel deste vídeo
  - /reel-inematds
  tamanho_skill_md: 7131
migracao:
  estagio: inventariado
  cluster: reels
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# reel-edita-inematds

## Descrição (do SKILL.md)

Converte um vídeo bruto vertical num reel/TikTok produzido com o estilo de INEMATDS — corta repetições/silêncios/erros, propõe um tratamento adaptado ao conteúdo, monta câmera alternando entre PiP/tela-dividida + B-roll real/IA + texto + SFX marcados e o deixa pronto para subir. Use quando disserem "edita este vídeo para reel", "faz o reel deste vídeo", "/reel-inematds", ou passarem o caminho de um MP4 vertical para publicar em Reels/TikTok/Shorts.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Converte um vídeo bruto vertical num reel/TikTok produzido com o estilo de INEMATDS — corta repetições/silêncios/erros, propõe um tratamento adaptado ao conteú… |
| Entradas (gatilhos) | edita este vídeo para reel, faz o reel deste vídeo, /reel-inematds |
| Ferramentas citadas | ffmpeg, groq, hyperframes, python, telegram, whisper |
| Processo (cabeçalhos) | reel-edita-INEMATDS — Bruto vertical → reel produzido → Regras de ouro (leia antes de tudo) → Entrada e workspace → FASE 1 — BLOQUEAR O CORTE (determinístico) · `references/01-corte-e-limpeza.md` → FASE 1.5 — LER O VÍDEO E PROPOR TRATAMENTO · `references/04-recetas.md` → FASE 2 — PLANEJAR A MONTAGEM · `references/02-motion-graphics.md` → FASE 3 — CONSTRUIR (Hyperframes) · `references/02-motion-graphics.md` + estilo + identidade → FASE 4 — SFX, QC E ENTREGA · `references/03-sfx-e-qc.md` → FASE 5 — REVISOR (subagente independente, OBRIGATÓRIO) · `references/05-revisor.md` → Regras que não se negociam |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references, scripts · SKILL.md com 7,131 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/captions.py`
- `scripts/cut.py`
- `scripts/islands.py`
- `scripts/lint-timeline.py`
- `scripts/make-sfx.sh`
- `scripts/mix-sfx.py`
- `scripts/verify-cut.py`

## Cluster

[reels](../clusters/reels.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
