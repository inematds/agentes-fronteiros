---
type: Skill
title: heygen-mcp
description: 'Vídeo de avatar falante no HeyGen gastando os CRÉDITOS DA ASSINATURA (via MCP), não o wallet de API. Gatilho: "pela assinatura", "sem gastar API", "via mcp". A irmã heygen-cli faz o mesmo
  via API key. Também conecta/che…'
resource: file:///home/nmaldaner/.claude/skills/heygen-mcp/SKILL.md
tags:
- skill
- avatar
sources:
- path: /home/nmaldaner/.claude/skills/heygen-mcp/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/avatar
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - scripts
  scripts:
  - scripts/deliver.mjs
  ferramentas:
  - heygen
  - mcp
  - node
  - telegram
  gatilhos:
  - pela assinatura
  - sem gastar API
  - via mcp
  tamanho_skill_md: 5095
migracao:
  estagio: inventariado
  cluster: avatar
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# heygen-mcp

## Descrição (do SKILL.md)

Vídeo de avatar falante no HeyGen gastando os CRÉDITOS DA ASSINATURA (via MCP), não o wallet de API. Gatilho: "pela assinatura", "sem gastar API", "via mcp". A irmã heygen-cli faz o mesmo via API key. Também conecta/checa o conector MCP do HeyGen.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Vídeo de avatar falante no HeyGen gastando os CRÉDITOS DA ASSINATURA (via MCP), não o wallet de API. Gatilho: "pela assinatura", "sem gastar API", "via mcp". A… |
| Entradas (gatilhos) | pela assinatura, sem gastar API, via mcp |
| Ferramentas citadas | heygen, mcp, node, telegram |
| Processo (cabeçalhos) | heygen-mcp → Pré-requisito: o conector MCP precisa estar ligado → Confirmar que está batendo na assinatura → Gerar o vídeo → Entregar no Telegram |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 5,095 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/deliver.mjs`

## Cluster

[avatar](../clusters/avatar.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
