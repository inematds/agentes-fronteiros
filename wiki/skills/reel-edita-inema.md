---
type: Skill
title: reel-edita-inema
description: 'Monta o REEL EMPILHADO da marca INEMA (9:16) a partir de vídeos 16:9 — topo impactante, avatar no meio, explicativo na base. Modos: compor, gerar o explicativo, gerar visuais, e capa de impacto
  (retenção/gancho/viral).…'
resource: file:///home/nmaldaner/.claude/skills/reel-edita-inema/SKILL.md
tags:
- skill
- reels
sources:
- path: /home/nmaldaner/.claude/skills/reel-edita-inema/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:32:36Z'
status: draft
related:
- clusters/reels
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 32
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/captions.py
  - scripts/cut.py
  - scripts/detect-repeats.py
  - scripts/gen-imagem.py
  - scripts/hf.sh
  - scripts/islands.py
  - scripts/legendas.py
  - scripts/lint-timeline.py
  - scripts/make-sfx.sh
  - scripts/mix-sfx.py
  - scripts/montar-reel.py
  - scripts/montar.py
  - scripts/narra.sh
  - scripts/preparar.py
  - scripts/stack-9x16.sh
  - scripts/transcribe-groq.sh
  - scripts/verify-cut.py
  ferramentas:
  - ffmpeg
  - flux
  - groq
  - heygen
  - hyperframes
  - inemavox
  - python
  - telegram
  - whisper
  gatilhos:
  - faz o reel disso
  tamanho_skill_md: 9364
migracao:
  estagio: mapeado
  cluster: reels
  destino: reels
  notas: piloto 1 — contrato em migracao/contratos/reels.yaml
  atualizado: '2026-09-14'
---

# reel-edita-inema

## Descrição (do SKILL.md)

Monta o REEL EMPILHADO da marca INEMA (9:16) a partir de vídeos 16:9 — topo impactante, avatar no meio, explicativo na base. Modos: compor, gerar o explicativo, gerar visuais, e capa de impacto (retenção/gancho/viral). Gatilho: "faz o reel disso", ou um MP4 de avatar 16:9.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Monta o REEL EMPILHADO da marca INEMA (9:16) a partir de vídeos 16:9 — topo impactante, avatar no meio, explicativo na base. Modos: compor, gerar o explicativo… |
| Entradas (gatilhos) | faz o reel disso |
| Ferramentas citadas | ffmpeg, flux, groq, heygen, hyperframes, inemavox, python, telegram, whisper |
| Processo (cabeçalhos) | reel-edita-inema — Vídeos 16:9 → reel empilhado INEMA → Regras de ouro (leia antes de tudo) → Entrada, modo e workspace → FASE 1 — (se precisar) BLOQUEAR O CORTE · `references/01-corte-e-limpeza.md` → FASE 1.5 — LER E PROPOR TRATAMENTO · `references/04-recetas.md` → FASE 2 — PREPARAR AS PEÇAS (conforme o modo) · `references/09-modos.md` → FASE 3 — COMPOR O EMPILHADO · `references/10-composicao-empilhada.md` → FASE 4 — SFX, QC E ENTREGA · `references/03-sfx-e-qc.md` → FASE 5 — REVISOR (subagente independente, OBRIGATÓRIO) · `references/05-revisor.md` → Regras que não se negociam |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 9,364 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/captions.py`
- `scripts/cut.py`
- `scripts/detect-repeats.py`
- `scripts/gen-imagem.py`
- `scripts/hf.sh`
- `scripts/islands.py`
- `scripts/legendas.py`
- `scripts/lint-timeline.py`
- `scripts/make-sfx.sh`
- `scripts/mix-sfx.py`
- `scripts/montar-reel.py`
- `scripts/montar.py`
- `scripts/narra.sh`
- `scripts/preparar.py`
- `scripts/stack-9x16.sh`
- `scripts/transcribe-groq.sh`
- `scripts/verify-cut.py`

## Cluster

[reels](../clusters/reels.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
