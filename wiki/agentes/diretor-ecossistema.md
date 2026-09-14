---
type: Agente
title: diretor-ecossistema
description: 'Roteador de decisão do ecossistema de vídeo do usuário. Use SEMPRE que houver dúvida sobre QUAL ferramenta usar para um pedido de vídeo/imagem/prompt entre: pixflow (render código aberto,
  sem IA), mdd (direção+storyboar…'
resource: file:///home/nmaldaner/.claude/agents/diretor-ecossistema.md
tags:
- agente
- subagente
sources:
- path: /home/nmaldaner/.claude/agents/diretor-ecossistema.md
  author: human:nei
  last_modified: '2026-06-07'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
agente:
  modelo: sonnet
  tools: ''
  tamanho: 3820
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# diretor-ecossistema

## Descrição

Roteador de decisão do ecossistema de vídeo do usuário. Use SEMPRE que houver dúvida sobre QUAL ferramenta usar para um pedido de vídeo/imagem/prompt entre: pixflow (render código aberto, sem IA), mdd (direção+storyboard p/ geradores IA como Seedance/Kling/Veo), video-plan-editor (plano de vídeo viral/beat sheet), promptprof (refino de prompt cinematográfico). Acione quando o usuário pedir um vídeo/filme e não estiver claro o caminho, quando pedir 'qual usar', 'qual a melhor ferramenta', 'como faço esse vídeo', ou quando o pedido misturar estratégia + direção + render. Retorna a decisão (qual ferramenta, em que ordem) com justificativa.

## Mapa

| Campo | Valor |
|---|---|
| Modelo | sonnet |
| Tools | todas |
| Seções | As 4 ferramentas → Eixo de decisão central: IA vs Código aberto → Regras de roteamento → Pipelines de referência → Formato da resposta |
| Destino provável | `agent/subagents/` (contexto isolado por desenho) |

## Notas de migração

_(vazio)_
