---
type: Skill
title: session-handoff
description: Use when the user wants to end a session and hand off context to a future agent. Triggers include "session handoff", "handoff", "wrap up", "wrap up session", "vou dar /clear", "encerrar sessão",
  "passar para outro agent…
resource: file:///home/nmaldaner/.claude/skills/session-handoff/SKILL.md
tags:
- skill
- conselho
sources:
- path: /home/nmaldaner/.claude/skills/session-handoff/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/conselho
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas: []
  gatilhos:
  - session handoff
  - handoff
  - wrap up
  - wrap up session
  - vou dar /clear
  - encerrar sessão
  - passar para outro agente
  - resumo final antes de limpar
  - summarize before clear
  tamanho_skill_md: 5170
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# session-handoff

## Descrição (do SKILL.md)

Use when the user wants to end a session and hand off context to a future agent. Triggers include "session handoff", "handoff", "wrap up", "wrap up session", "vou dar /clear", "encerrar sessão", "passar para outro agente", "resumo final antes de limpar", "summarize before clear". Produces a chat-only structured handoff so a fresh agent can continue without losing continuity.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Use when the user wants to end a session and hand off context to a future agent. Triggers include "session handoff", "handoff", "wrap up", "wrap up session", "… |
| Entradas (gatilhos) | session handoff, handoff, wrap up, wrap up session, vou dar /clear, encerrar sessão, passar para outro agente, resumo final antes de limpar, summarize before clear |
| Ferramentas citadas | — |
| Processo (cabeçalhos) | Session Handoff → When to invoke → How to produce the summary → Confidence markers → Output template — use exactly this structure, every time → Session Handoff — <one-line title of what this session was about> → Where it started → Applied / shipped → Proposed / attempted but not confirmed → Key files for next session |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 5,170 chars |

## Cluster

[conselho](../clusters/conselho.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
