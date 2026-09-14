---
type: Skill
title: video-ia
description: 'Converte uma ideia de anúncio em vídeo gerado com IA, passo a passo: faz cinco perguntas, propõe dez conceitos com roteiro, e dos que você escolher escreve um Markdown por vídeo com o essencial
  pra gerar: as imagens que…'
resource: file:///home/nmaldaner/.claude/skills/video-ia/SKILL.md
tags:
- skill
- video-ia
sources:
- path: /home/nmaldaner/.claude/skills/video-ia/SKILL.md
  author: human:nei
  last_modified: '2026-09-06'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-ia
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 20
  subpastas:
  - marcas
  - references
  scripts: []
  ferramentas:
  - flux
  gatilhos:
  - /video-ia
  - faz um anúncio com IA
  - quero um vídeo com IA de…
  - me dá ideias de vídeo pra…
  - prompt pra Seedance / Agnes / Dreamina
  - ficha de personagem
  tamanho_skill_md: 5690
migracao:
  estagio: inventariado
  cluster: video-ia
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# video-ia

## Descrição (do SKILL.md)

Converte uma ideia de anúncio em vídeo gerado com IA, passo a passo: faz cinco perguntas, propõe dez conceitos com roteiro, e dos que você escolher escreve um Markdown por vídeo com o essencial pra gerar: as imagens que precisam ser criadas antes, o roteiro se você for gravar a voz, o que subir e em que ordem, e o prompt pronto pra colar. Usar quando alguém disser "/video-ia", "faz um anúncio com IA", "quero um vídeo com IA de…", "me dá ideias de vídeo pra…", "prompt pra Seedance / Agnes / Dreamina", "ficha de personagem", ou trouxer um roteiro já aprovado pra produzir. Não gera o vídeo, não gasta crédito e não publica.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Converte uma ideia de anúncio em vídeo gerado com IA, passo a passo: faz cinco perguntas, propõe dez conceitos com roteiro, e dos que você escolher escreve um… |
| Entradas (gatilhos) | /video-ia, faz um anúncio com IA, quero um vídeo com IA de…, me dá ideias de vídeo pra…, prompt pra Seedance / Agnes / Dreamina, ficha de personagem |
| Ferramentas citadas | flux |
| Processo (cabeçalhos) | /video-ia — da ideia ao prompt, em cinco passos → O fluxo · nesta ordem, sem pular passos → 1 · Escute a ideia → 2 · Cinco perguntas sobre a mensagem, de uma vez → 3 · O menu de dez → PARA → 4 · O técnico, só dos escolhidos → 5 · Um Markdown por vídeo escolhido → As regras duras → Fechamento no chat · duas linhas → Limites |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: marcas, references · SKILL.md com 5,690 chars |

## Cluster

[video-ia](../clusters/video-ia.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
