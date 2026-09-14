---
type: Skill
title: video-demonstrativo
description: 'Walkthrough narrado de uma aplicação web a partir do link: navega o app de verdade, captura as telas reais e monta o vídeo com moldura de navegador, cursor animado e zoom. MOSTRA um app real
  sendo usado — para explicar…'
resource: file:///home/nmaldaner/.claude/skills/video-demonstrativo/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/video-demonstrativo/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-explicativo
skill:
  versao: 1.1.0
  invocacao_pelo_modelo: true
  arquivos: 23
  subpastas:
  - assets
  - references
  - scripts
  scripts:
  - scripts/capture.mjs
  - scripts/composition-template.mjs
  - scripts/fetch-fonts.mjs
  - scripts/narration-template.sh
  ferramentas:
  - agent-browser
  - ffmpeg
  - flux
  - hyperframes
  - node
  - playwright
  - tts
  gatilhos: []
  tamanho_skill_md: 7849
migracao:
  estagio: inventariado
  cluster: video-explicativo
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# video-demonstrativo

## Descrição (do SKILL.md)

Walkthrough narrado de uma aplicação web a partir do link: navega o app de verdade, captura as telas reais e monta o vídeo com moldura de navegador, cursor animado e zoom. MOSTRA um app real sendo usado — para explicar um conceito com motion graphics, use video-explicativo.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Walkthrough narrado de uma aplicação web a partir do link: navega o app de verdade, captura as telas reais e monta o vídeo com moldura de navegador, cursor ani… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | agent-browser, ffmpeg, flux, hyperframes, node, playwright, tts |
| Processo (cabeçalhos) | Vídeo Demonstrativo (HyperFrames + captura de tela) → Princípio que rege tudo: capturar antes, animar depois → Pré-requisitos (já nesta máquina) → Fluxo (sempre nesta ordem) → Regras de ouro (não-negociáveis) → Limites conhecidos (seja honesto com o usuário) → CTA INEMA.CLUB (cena final padrão) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references, scripts · SKILL.md com 7,849 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/capture.mjs`
- `scripts/composition-template.mjs`
- `scripts/fetch-fonts.mjs`
- `scripts/narration-template.sh`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
