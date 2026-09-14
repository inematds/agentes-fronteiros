---
type: Skill
title: forja-reel
description: 'META-SKILL: entrevista você sobre estilo e identidade e gera A SUA própria skill "/reel-edita", com motor de corte e ritmo testado por dentro. NÃO edita um vídeo específico — quem edita é
  a skill que ESTA gera.'
resource: file:///home/nmaldaner/.claude/skills/forja-reel/SKILL.md
tags:
- skill
- reels
sources:
- path: /home/nmaldaner/.claude/skills/forja-reel/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/reels
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 17
  subpastas:
  - assets
  - references
  scripts:
  - assets/motor-scripts/captions.py
  - assets/motor-scripts/cut.py
  - assets/motor-scripts/fal-gen.py
  - assets/motor-scripts/islands.py
  - assets/motor-scripts/lint-timeline.py
  - assets/motor-scripts/make-sfx.sh
  - assets/motor-scripts/mix-sfx.py
  - assets/motor-scripts/verify-cut.py
  ferramentas:
  - ffmpeg
  - flux
  - groq
  - hyperframes
  - node
  - python
  - whisper
  gatilhos:
  - /reel-edita
  tamanho_skill_md: 5553
migracao:
  estagio: inventariado
  cluster: reels
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# forja-reel

## Descrição (do SKILL.md)

META-SKILL: entrevista você sobre estilo e identidade e gera A SUA própria skill "/reel-edita", com motor de corte e ritmo testado por dentro. NÃO edita um vídeo específico — quem edita é a skill que ESTA gera.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | META-SKILL: entrevista você sobre estilo e identidade e gera A SUA própria skill "/reel-edita", com motor de corte e ritmo testado por dentro. NÃO edita um víd… |
| Entradas (gatilhos) | /reel-edita |
| Ferramentas citadas | ffmpeg, flux, groq, hyperframes, node, python, whisper |
| Processo (cabeçalhos) | /forja-reel — Cria O SEU próprio editor de reels (meta-skill) → O que a pessoa precisa (resumo honesto antes de começar) → Fluxo (4 fases, em ordem) → FASE A — ENTREVISTA · `references/01-entrevista.md` → FASE B — DIAGNÓSTICO DE AMBIENTE · `references/02-diagnostico-de-ambiente.md` → FASE C — GERAR A SKILL · `references/03-geracao.md` + `references/04-modelo-skill-filha.md` → FASE D — ESTREIA → Regras que não se negociam |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 5,553 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/motor-scripts/captions.py`
- `assets/motor-scripts/cut.py`
- `assets/motor-scripts/fal-gen.py`
- `assets/motor-scripts/islands.py`
- `assets/motor-scripts/lint-timeline.py`
- `assets/motor-scripts/make-sfx.sh`
- `assets/motor-scripts/mix-sfx.py`
- `assets/motor-scripts/verify-cut.py`

## Cluster

[reels](../clusters/reels.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
