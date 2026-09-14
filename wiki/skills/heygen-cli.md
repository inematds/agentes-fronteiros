---
type: Skill
title: heygen-cli
description: Roteiro de texto vira vídeo de AVATAR FALANTE no HeyGen (via API key), MP4 entregue no Telegram. Também lista vozes, avatares e looks. Render é pago — confirmar antes. Pelos créditos da assinatura,
  use heygen-mcp. Não é…
resource: file:///home/nmaldaner/.claude/skills/heygen-cli/SKILL.md
tags:
- skill
- avatar
sources:
- path: /home/nmaldaner/.claude/skills/heygen-cli/SKILL.md
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
  - scripts/heygen.mjs
  ferramentas:
  - flux
  - heygen
  - mcp
  - node
  - telegram
  gatilhos: []
  tamanho_skill_md: 4652
migracao:
  estagio: inventariado
  cluster: avatar
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# heygen-cli

## Descrição (do SKILL.md)

Roteiro de texto vira vídeo de AVATAR FALANTE no HeyGen (via API key), MP4 entregue no Telegram. Também lista vozes, avatares e looks. Render é pago — confirmar antes. Pelos créditos da assinatura, use heygen-mcp. Não é para explicativo sem rosto nem motion graphics.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Roteiro de texto vira vídeo de AVATAR FALANTE no HeyGen (via API key), MP4 entregue no Telegram. Também lista vozes, avatares e looks. Render é pago — confirma… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | flux, heygen, mcp, node, telegram |
| Processo (cabeçalhos) | heygen-cli → Quando usar → Como gerar → Opções → Descobrir vozes, avatares e looks → Pontos importantes (porquês) → Config |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 4,652 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/heygen.mjs`

## Cluster

[avatar](../clusters/avatar.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
