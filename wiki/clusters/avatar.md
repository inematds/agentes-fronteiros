---
type: Cluster
title: Avatar falante (HeyGen)
description: 5 skills disputam a intenção “Avatar falante (HeyGen)”.
tags:
- cluster
- avatar
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/avatar-heygen-nei
- skills/dublagem-compasso
- skills/heygen-cli
- skills/heygen-mcp
- skills/heygen-video-nei
cluster:
  id: avatar
  membros:
  - avatar-heygen-nei
  - dublagem-compasso
  - heygen-cli
  - heygen-mcp
  - heygen-video-nei
---

# Cluster: Avatar falante (HeyGen)

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [avatar-heygen-nei](../skills/avatar-heygen-nei.md) | Gera vídeo do avatar falante do Nei no HeyGen escolhendo entre os LOOKS/personagens dele (velho, beje, frio,… | 0 | heygen, mcp, node |
| [dublagem-compasso](../skills/dublagem-compasso.md) | Redubla um vídeo de personagem falando (Kling, Veo, Seedance) com voz clonada local, alinhando a fala nas bat… | 0 | chatterbox, ffmpeg, inemavox, kling, python |
| [heygen-cli](../skills/heygen-cli.md) | Roteiro de texto vira vídeo de AVATAR FALANTE no HeyGen (via API key), MP4 entregue no Telegram. Também lista… | 1 | flux, heygen, mcp, node, telegram |
| [heygen-mcp](../skills/heygen-mcp.md) | Vídeo de avatar falante no HeyGen gastando os CRÉDITOS DA ASSINATURA (via MCP), não o wallet de API. Gatilho:… | 1 | heygen, mcp, node, telegram |
| [heygen-video-nei](../skills/heygen-video-nei.md) | Cria um vídeo de avatar na HeyGen pelo navegador (extensão Claude in Chrome/Edge) usando o avatar "Nei Maldan… | 0 | heygen |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`heygen` (4×), `mcp` (3×), `node` (3×), `telegram` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
