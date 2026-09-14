---
type: Skill
title: video-explicativo
description: Cria vídeos explicativos completos em PT-BR (HTML→MP4 via HyperFrames) a partir de um assunto — roteiro, narração TTS local, cenas animadas dark premium, captions e CTA do INEMA.CLUB, nos formatos
  16:9 (YouTube) e 9:16…
resource: file:///home/nmaldaner/.claude/skills/video-explicativo/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/video-explicativo/SKILL.md
  author: human:nei
  last_modified: '2026-07-21'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:32:36Z'
status: draft
related:
- clusters/video-explicativo
skill:
  versao: 1.11.3
  invocacao_pelo_modelo: true
  arquivos: 29
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/composition-template.mjs
  - scripts/fetch-fonts.mjs
  - scripts/narration-template.sh
  ferramentas:
  - chatterbox
  - ffmpeg
  - flux
  - github
  - heygen
  - hyperframes
  - inemavox
  - node
  - python
  - tts
  gatilhos:
  - fazer um vídeo
  - vídeo explicativo
  - vídeo sobre X
  - vídeo pra Shorts/Reels
  - mini tutorial em vídeo
  - vídeo do INEMA
  tamanho_skill_md: 14727
migracao:
  estagio: mapeado
  cluster: video-explicativo
  destino: video-explicativo
  notas: piloto 2 — contrato em migracao/contratos/video-explicativo.yaml
  atualizado: '2026-09-14'
---

# video-explicativo

## Descrição (do SKILL.md)

Cria vídeos explicativos completos em PT-BR (HTML→MP4 via HyperFrames) a partir de um assunto — roteiro, narração TTS local, cenas animadas dark premium, captions e CTA do INEMA.CLUB, nos formatos 16:9 (YouTube) e 9:16 (Shorts/Reels). Use quando o usuário pedir para "fazer um vídeo", "vídeo explicativo", "vídeo sobre X", "vídeo pra Shorts/Reels", "mini tutorial em vídeo", "vídeo do INEMA", ou quando der um assunto e quiser um vídeo narrado pronto. Cobre roteiro, locução, animação, render e a CTA final.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Cria vídeos explicativos completos em PT-BR (HTML→MP4 via HyperFrames) a partir de um assunto — roteiro, narração TTS local, cenas animadas dark premium, capti… |
| Entradas (gatilhos) | fazer um vídeo, vídeo explicativo, vídeo sobre X, vídeo pra Shorts/Reels, mini tutorial em vídeo, vídeo do INEMA |
| Ferramentas citadas | chatterbox, ffmpeg, flux, github, heygen, hyperframes, inemavox, node, python, tts |
| Processo (cabeçalhos) | Vídeo Explicativo (HyperFrames) → Pré-requisitos (já instalados nesta máquina) → Plano de cenas (quantas cenas?) → Variações (quando pedem "me dá 2/3 versões") → Fluxo (sempre nesta ordem) → Regras de ouro (não-negociáveis) → Identidade visual (house style) → CTA INEMA.CLUB (cena final padrão) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 14,727 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/composition-template.mjs`
- `scripts/fetch-fonts.mjs`
- `scripts/narration-template.sh`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
