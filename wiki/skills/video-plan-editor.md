---
type: Skill
title: video-plan-editor
description: Cria um plano profissional de vídeo de ALTA PERFORMANCE a partir de um assunto ou link, usando uma base de conhecimento (estratégia viral + linguagem de câmera + prompting cinematográfico +
  motion graphics premium). Det…
resource: file:///home/nmaldaner/.claude/skills/video-plan-editor/SKILL.md
tags:
- skill
- video-ia
sources:
- path: /home/nmaldaner/.claude/skills/video-plan-editor/SKILL.md
  author: human:nei
  last_modified: '2026-06-07'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-ia
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - examples
  scripts: []
  ferramentas:
  - agent-browser
  - ffmpeg
  - flux
  - hyperframes
  - kling
  - veo
  gatilhos:
  - plano de vídeo
  - plano de edição
  - editar vídeo
  - clipe
  - corte para Reels/TikTok
  - vídeo promocional/de vendas/viral
  tamanho_skill_md: 5875
migracao:
  estagio: inventariado
  cluster: video-ia
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# video-plan-editor

## Descrição (do SKILL.md)

Cria um plano profissional de vídeo de ALTA PERFORMANCE a partir de um assunto ou link, usando uma base de conhecimento (estratégia viral + linguagem de câmera + prompting cinematográfico + motion graphics premium). Detecta o input, define a estratégia, escolhe preset e emite plano-edicao.json + RESUMO.md. Render opcional via motion graphics (HyperFrames) + b-roll flux2-klein. Use quando o usuário der um assunto/link e pedir "plano de vídeo", "plano de edição", "editar vídeo", "clipe", "corte para Reels/TikTok", "vídeo promocional/de vendas/viral", ou um vídeo de alta performance.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Cria um plano profissional de vídeo de ALTA PERFORMANCE a partir de um assunto ou link, usando uma base de conhecimento (estratégia viral + linguagem de câmera… |
| Entradas (gatilhos) | plano de vídeo, plano de edição, editar vídeo, clipe, corte para Reels/TikTok, vídeo promocional/de vendas/viral |
| Ferramentas citadas | agent-browser, ffmpeg, flux, hyperframes, kling, veo |
| Processo (cabeçalhos) | video-plan-editor → Pré-requisitos → Base de conhecimento (consultar nesta ordem de raciocínio) → Fluxo (sempre nesta ordem) → Presets (perfis de parâmetro — ver `pacing.md`) → Regras de ouro |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: examples · SKILL.md com 5,875 chars |

## Cluster

[video-ia](../clusters/video-ia.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
