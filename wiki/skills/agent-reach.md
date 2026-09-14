---
type: Skill
title: agent-reach
description: 'Fetches internet content: general web research, plus 13 platforms (X, Reddit, YouTube, GitHub, LinkedIn, Bilibili, XiaoHongShu, V2EX, RSS…). Use when asked to research a topic or when a URL
  is shared. FETCHES only — not…'
resource: file:///home/nmaldaner/.claude/skills/agent-reach/SKILL.md
tags:
- skill
- pesquisa-web
sources:
- path: /home/nmaldaner/.claude/skills/agent-reach/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pesquisa-web
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 7
  subpastas:
  - references
  scripts: []
  ferramentas:
  - github
  - mcp
  - yt-dlp
  gatilhos: []
  tamanho_skill_md: 4357
migracao:
  estagio: inventariado
  cluster: pesquisa-web
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# agent-reach

## Descrição (do SKILL.md)

Fetches internet content: general web research, plus 13 platforms (X, Reddit, YouTube, GitHub, LinkedIn, Bilibili, XiaoHongShu, V2EX, RSS…). Use when asked to research a topic or when a URL is shared. FETCHES only — not for writing reports, posting or commenting.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Fetches internet content: general web research, plus 13 platforms (X, Reddit, YouTube, GitHub, LinkedIn, Bilibili, XiaoHongShu, V2EX, RSS…). Use when asked to… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, mcp, yt-dlp |
| Processo (cabeçalhos) | Agent Reach — internet capability router → Standing rules (apply for the whole session) → Routing table → Zero-config quick commands → Exa web search → Read any web page → GitHub search → YouTube subtitles (NOTE: never use yt-dlp for Bilibili — see video.md) → V2EX hot topics → Bilibili search (bili-cli, no login needed) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 4,357 chars |

## Cluster

[pesquisa-web](../clusters/pesquisa-web.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
