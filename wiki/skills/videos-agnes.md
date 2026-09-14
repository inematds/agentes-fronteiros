---
type: Skill
title: videos-agnes
description: História/conto → filme animado narrado em PT-BR via Agnes AI (US$ 0), entregue no Telegram do openpcbot. Caminho simples e direto. Se pedir DIREÇÃO (decupagem, câmera, ritmo) ou escolher provedor,
  use videoanima. Imagem…
resource: file:///home/nmaldaner/.claude/skills/videos-agnes/SKILL.md
tags:
- skill
- imagens
sources:
- path: /home/nmaldaner/.claude/skills/videos-agnes/SKILL.md
  author: human:nei
  last_modified: '2026-09-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/imagens
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - chatterbox
  - ffmpeg
  - flux
  - inemavox
  - python
  - telegram
  - tts
  gatilhos: []
  tamanho_skill_md: 4612
migracao:
  estagio: inventariado
  cluster: imagens
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# videos-agnes

## Descrição (do SKILL.md)

História/conto → filme animado narrado em PT-BR via Agnes AI (US$ 0), entregue no Telegram do openpcbot. Caminho simples e direto. Se pedir DIREÇÃO (decupagem, câmera, ritmo) ou escolher provedor, use videoanima. Imagem avulsa é imagens-agnes.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | História/conto → filme animado narrado em PT-BR via Agnes AI (US$ 0), entregue no Telegram do openpcbot. Caminho simples e direto. Se pedir DIREÇÃO (decupagem,… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | chatterbox, ffmpeg, flux, inemavox, python, telegram, tts |
| Processo (cabeçalhos) | videos-agnes — história → filme narrado (Agnes AI, US$ 0) → Fluxo → REGRA: revisar o texto antes da narração (`revisao.py`, automático) → Para uma história NOVA → Regras não-óbvias (medidas — ver `~/projetos/agnes-nei/NOTAS-API.md`) → Limitações conhecidas (avisar o usuário, não esconder) → Pré-requisitos |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 4,612 chars |

## Cluster

[imagens](../clusters/imagens.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
