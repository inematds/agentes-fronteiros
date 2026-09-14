---
type: Cluster
title: Pesquisa / navegação / extração web
description: 6 skills disputam a intenção “Pesquisa / navegação / extração web”.
tags:
- cluster
- pesquisa-web
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/agent-browser
- skills/agent-reach
- skills/clima
- skills/espiona-ads
- skills/pp-skool
- skills/website-intelligence
cluster:
  id: pesquisa-web
  membros:
  - agent-browser
  - agent-reach
  - clima
  - espiona-ads
  - pp-skool
  - website-intelligence
---

# Cluster: Pesquisa / navegação / extração web

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [agent-browser](../skills/agent-browser.md) | Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the… | 0 | agent-browser |
| [agent-reach](../skills/agent-reach.md) | Fetches internet content: general web research, plus 13 platforms (X, Reddit, YouTube, GitHub, LinkedIn, Bili… | 0 | github, mcp, yt-dlp |
| [clima](../skills/clima.md) | Clima atual e previsão (até 16 dias) de qualquer cidade via Open-Meteo, sem API key, em PT-BR. Vale também pa… | 1 | node |
| [espiona-ads](../skills/espiona-ads.md) | Espiona os anúncios de uma conta na Biblioteca de Anúncios da Meta e faz engenharia reversa da fórmula dela:… | 2 | agent-browser, ffmpeg, groq, mcp, whisper |
| [pp-skool](../skills/pp-skool.md) | Read Skool community data — posts, members, events — with local cache and topic summaries. | 0 | heygen, mcp, node |
| [website-intelligence](../skills/website-intelligence.md) | Research-driven competitive intelligence engine for websites. Scrapes a client's existing site, analyzes thei… | 0 | mcp, vercel |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`mcp` (4×), `agent-browser` (2×), `node` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
