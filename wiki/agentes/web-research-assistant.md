---
type: Agente
title: web-research-assistant
description: Use this agent when the user needs to gather information from the web, conduct research on a topic, find specific data or facts online, or needs help formulating effective search queries. This
  includes requests for curr…
resource: file:///home/nmaldaner/.claude/agents/web-research-assistant.md
tags:
- agente
- subagente
sources:
- path: /home/nmaldaner/.claude/agents/web-research-assistant.md
  author: human:nei
  last_modified: '2026-01-24'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
agente:
  modelo: sonnet
  tools: ''
  tamanho: 5071
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# web-research-assistant

## Descrição

Use this agent when the user needs to gather information from the web, conduct research on a topic, find specific data or facts online, or needs help formulating effective search queries. This includes requests for current information, comparative research, fact-checking, or exploratory investigation of any subject.\n\nExamples:\n\n<example>\nContext: User needs to research a technical topic\nuser: "Preciso entender as diferenças entre React e Vue.js para um projeto"\nassistant: "Vou usar o agente de pesquisa web para investigar as diferenças entre React e Vue.js"\n<commentary>\nSince the user needs comparative information about technologies, use the Task tool to launch the web-research-assistant agent to conduct thorough research.\n</commentary>\n</example>\n\n<example>\nContext: User asks about current events or recent information\nuser: "Quais são as últimas tendências em inteligência artificial em 2024?"\nassistant: "Vou acionar o agente de pesquisa web para buscar as tendências mais recentes em IA"\n<commentary>\nSince the user needs current, up-to-date information that requires web research, use the Task tool to launch the web-research-assistant agent.\n</commentary>\n</example>\n\n<example>\nContext: User needs to verify facts or find specific data\nuser: "Qual é a população atual do Brasil e como se compara com outros países da América do Sul?"\nassistant: "Vou utilizar o agente de pesquisa web para encontrar dados demográficos atualizados"\n<commentary>\nSince the user needs factual data that requires verification from reliable sources, use the Task tool to launch the web-research-assistant agent to gather accurate information.\n</commentary>\n</example>

## Mapa

| Campo | Valor |
|---|---|
| Modelo | sonnet |
| Tools | todas |
| Seções | Sua Identidade e Expertise → Suas Responsabilidades Principais → Diretrizes de Qualidade → Formato de Resposta → Comportamento Proativo → Idioma |
| Destino provável | `agent/subagents/` (contexto isolado por desenho) |

## Notas de migração

_(vazio)_
