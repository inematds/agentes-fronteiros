---
type: Skill
title: espiona-ads
description: 'Espiona os anúncios de uma conta na Biblioteca de Anúncios da Meta e faz engenharia reversa da fórmula dela: extrai todos os anúncios ativos com copy, datas e URLs de vídeo em HD, ranqueia
  por sinais de que estão funcio…'
resource: file:///home/nmaldaner/.claude/skills/espiona-ads/SKILL.md
tags:
- skill
- pesquisa-web
sources:
- path: /home/nmaldaner/.claude/skills/espiona-ads/SKILL.md
  author: human:nei
  last_modified: '2026-09-06'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pesquisa-web
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 4
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/extrai.js
  - scripts/processa.sh
  ferramentas:
  - agent-browser
  - ffmpeg
  - groq
  - mcp
  - whisper
  gatilhos:
  - /espiona-ads
  - espiona esses anúncios
  - analisa os anúncios de [marca]
  - olha o que a concorrência está fazendo na Meta
  - que anúncios X tem
  - biblioteca de anúncios de
  - ads library de
  - que criativos ela usa
  - como são os anúncios do meu concorrente
  - isso é feito com IA?
  tamanho_skill_md: 9464
migracao:
  estagio: inventariado
  cluster: pesquisa-web
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# espiona-ads

## Descrição (do SKILL.md)

Espiona os anúncios de uma conta na Biblioteca de Anúncios da Meta e faz engenharia reversa da fórmula dela: extrai todos os anúncios ativos com copy, datas e URLs de vídeo em HD, ranqueia por sinais de que estão funcionando (dias em circulação e nº de variantes vivas), baixa os vídeos, mede (cortes de cena, palavras por minuto), transcreve com Whisper, analisa frame a frame com subagentes, e devolve um playbook acionável: banco de hooks literais, esqueleto persuasivo minutado, veredito sobre se estão usando IA generativa (com evidência, não a olho), e o que é transplantável. USAR SEMPRE que o usuário disser "/espiona-ads", "espiona esses anúncios", "analisa os anúncios de [marca]", "olha o que a concorrência está fazendo na Meta", "que anúncios X tem", "biblioteca de anúncios de", "ads library de", "que criativos ela usa", "como são os anúncios do meu concorrente", ou colar uma URL de facebook.com/ads/library. Também se perguntar "isso é feito com IA?" sobre anúncios de outra marca. NÃO é pra analisar o DESEMPENHO dos anúncios próprios de quem usa a skill (pra isso precisa ler os dados exportados do Gerenciador de Anúncios) nem pra editar vídeo.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Espiona os anúncios de uma conta na Biblioteca de Anúncios da Meta e faz engenharia reversa da fórmula dela: extrai todos os anúncios ativos com copy, datas e… |
| Entradas (gatilhos) | /espiona-ads, espiona esses anúncios, analisa os anúncios de [marca], olha o que a concorrência está fazendo na Meta, que anúncios X tem, biblioteca de anúncios de, ads library de, que criativos ela usa, como são os anúncios do meu concorrente, isso é feito com IA? |
| Ferramentas citadas | agent-browser, ffmpeg, groq, mcp, whisper |
| Processo (cabeçalhos) | /espiona-ads — Engenharia reversa dos anúncios de uma conta → O que você precisa → Entrada → FASE 1 — Extração (você faz, não delegue: são 3 chamadas) → FASE 2 — Ranking → FASE 3 — Processo mecânico (script, sem LLM) → FASE 4 — Análise com subagentes → FASE 5 — Contexto do funil (você) → FASE 6 — Síntese (você, e só você) → Erros que já foram cometidos (não repita) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 9,464 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/extrai.js`
- `scripts/processa.sh`

## Cluster

[pesquisa-web](../clusters/pesquisa-web.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
