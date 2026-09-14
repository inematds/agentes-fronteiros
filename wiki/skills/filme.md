---
type: Skill
title: filme
description: 'historia.json (do skill roteiro) vira FILME narrado em parallax 2.5D no pixflow — camera por emocao, musica e SFX, sem IA de video. Gatilho: "faz o filme", "renderiza o filme". NAO escreve
  a historia (isso e o skill rot…'
resource: file:///home/nmaldaner/.claude/skills/filme/SKILL.md
tags:
- skill
- pixflow
sources:
- path: /home/nmaldaner/.claude/skills/filme/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pixflow
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 13
  subpastas:
  - exemplo
  - knowledge
  - scripts
  - templates
  scripts:
  - exemplo/avatar-eco-cinzas-v2/build.mjs
  - exemplo/avatar-eco-cinzas-v2/build_sfx.py
  - exemplo/avatar-eco-cinzas-v2/narra2.py
  - scripts/baixar_musica.sh
  - scripts/build_sfx.py
  - scripts/engine.mjs
  - scripts/mux.sh
  - templates/decupagem.template.mjs
  - templates/narracao.template.py
  ferramentas:
  - ffmpeg
  - flux
  - inemavox
  - node
  - pixflow
  - python
  - telegram
  - tts
  - yt-dlp
  gatilhos:
  - faz o filme
  - renderiza o filme
  tamanho_skill_md: 3687
migracao:
  estagio: inventariado
  cluster: pixflow
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# filme

## Descrição (do SKILL.md)

historia.json (do skill roteiro) vira FILME narrado em parallax 2.5D no pixflow — camera por emocao, musica e SFX, sem IA de video. Gatilho: "faz o filme", "renderiza o filme". NAO escreve a historia (isso e o skill roteiro).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | historia.json (do skill roteiro) vira FILME narrado em parallax 2.5D no pixflow — camera por emocao, musica e SFX, sem IA de video. Gatilho: "faz o filme", "re… |
| Entradas (gatilhos) | faz o filme, renderiza o filme |
| Ferramentas citadas | ffmpeg, flux, inemavox, node, pixflow, python, telegram, tts, yt-dlp |
| Processo (cabeçalhos) | filme → Pré-requisitos (sondar antes) → Fluxo → Regras de direção (resumo — detalhe em knowledge/direcao.md) → Roadmap → Exemplo completo |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: exemplo, knowledge, scripts, templates · SKILL.md com 3,687 chars |

## Scripts (candidatos a `agent/tools/`)

- `exemplo/avatar-eco-cinzas-v2/build.mjs`
- `exemplo/avatar-eco-cinzas-v2/build_sfx.py`
- `exemplo/avatar-eco-cinzas-v2/narra2.py`
- `scripts/baixar_musica.sh`
- `scripts/build_sfx.py`
- `scripts/engine.mjs`
- `scripts/mux.sh`
- `templates/decupagem.template.mjs`
- `templates/narracao.template.py`

## Cluster

[pixflow](../clusters/pixflow.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
