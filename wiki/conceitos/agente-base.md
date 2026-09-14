---
type: Conceito
title: Agente base (INEMA AGENT)
description: O agente generalista que substitui os agentes especializados — identifica intenção, escolhe skill, carrega contexto, chama ferramentas, executa, valida e aprende.
tags: [agente-base, generalista, jarvis]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: draft
related: [conceitos/plano-migracao, conceitos/router, conceitos/eve-vercel]
---

# Agente base

```text
INEMA AGENT → identifica intenção → escolhe SKILL → carrega contexto necessário
            → chama ferramentas → executa → valida → entrega → aprende
```

Sabe trabalhar com: arquivos, terminal, web, MCP, APIs, memória (wiki + memória do Claude Code), skills.

Prompt sempre-ligado: `agent/instructions.md`. Config: `agent/agent.yaml`.

## O que NÃO é
- Não é mais um agente especializado. Os especialistas viram skills (procedimentos) ou subagentes só quando precisam de contexto isolado por desenho (ex.: Conselho de Agentes).
- Não reescreve código utilitário: manda executar `agent/tools/*`.

## Substituição prevista
| Agente/skill hoje | Vira |
|---|---|
| `video-explicativo`, `videoprodutor`, `faceless-explainer` | skill `video-explicativo` com references por variante |
| `reel-edita-inema`, `reel-edita-inematds`, `forja-reel` | skill `reels` (modos: empilhado INEMA · talking-head INEMATDS) |
| `formato-curso-v5` / `v2` | skill `curso` (v5 leigo · v2 dark âmbar); v1/v3/v4 só manutenção |
| `maestro-roteador`, `diretor-ecossistema` | absorvidos na seção Router do `instructions.md` |
| Conselho (`mestre-do-conselho` + membros) | permanecem em `agent/subagents/` |
