---
type: Agente
title: triple-x-responder
description: 'Use this agent when the user sends a message containing only ''xxx'' or similar placeholder text that appears to be incomplete, accidental, or requires clarification. Examples:\n\n<example>\nContext:
  User sends an incompl…'
resource: file:///home/nmaldaner/.claude/agents/triple-x-responder.md
tags:
- agente
- subagente
sources:
- path: /home/nmaldaner/.claude/agents/triple-x-responder.md
  author: human:nei
  last_modified: '2026-01-24'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:32:36Z'
status: draft
agente:
  modelo: sonnet
  tools: ''
  tamanho: 2869
migracao:
  estagio: descontinuado
  cluster: conselho
  destino: ''
  notas: placeholder sem função operacional
  atualizado: '2026-09-14'
---

# triple-x-responder

## Descrição

Use this agent when the user sends a message containing only 'xxx' or similar placeholder text that appears to be incomplete, accidental, or requires clarification. Examples:\n\n<example>\nContext: User sends an incomplete or placeholder message.\nuser: "xxx"\nassistant: "I notice you've sent 'xxx' which appears to be a placeholder or incomplete message. Let me use the triple-x-responder agent to handle this appropriately."\n<commentary>\nSince the user sent what appears to be placeholder text, use the triple-x-responder agent to politely request clarification.\n</commentary>\n</example>\n\n<example>\nContext: User sends a message that seems to be testing or accidentally submitted.\nuser: "xxxx"\nassistant: "This looks like it might have been sent accidentally. I'll use the triple-x-responder agent to help clarify what you need."\n<commentary>\nThe message appears to be a test or accidental submission, so use the triple-x-responder agent to seek clarification.\n</commentary>\n</example>

## Mapa

| Campo | Valor |
|---|---|
| Modelo | sonnet |
| Tools | todas |
| Seções | Your Approach → Response Guidelines → Example Response Structure → Quality Checks |
| Destino provável | `agent/subagents/` (contexto isolado por desenho) |

## Notas de migração

_(vazio)_
