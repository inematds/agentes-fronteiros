---
type: Skill
title: polyskill
description: Cross-runtime skill optimizer. Use this skill when the user wants to package an Agent Skill so it runs in both Claude Code and OpenAI Codex from a single portable source. Also use when the
  user wants to import an existi…
resource: file:///home/nmaldaner/.claude/skills/polyskill/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/polyskill/SKILL.md
  author: human:nei
  last_modified: '2026-05-22'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - gemini
  - github
  - mcp
  - openai
  gatilhos: []
  tamanho_skill_md: 6816
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# polyskill

## Descrição (do SKILL.md)

Cross-runtime skill optimizer. Use this skill when the user wants to package an Agent Skill so it runs in both Claude Code and OpenAI Codex from a single portable source. Also use when the user wants to import an existing skill (Claude Code or Codex) into the portable format, build/emit for any runtime, install a skill into Claude Code or Codex, or troubleshoot why a skill behaves differently across runtimes.


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Cross-runtime skill optimizer. Use this skill when the user wants to package an Agent Skill so it runs in both Claude Code and OpenAI Codex from a single porta… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | gemini, github, mcp, openai |
| Processo (cabeçalhos) | polyskill — Cross-Runtime Skill Optimizer → When this skill should run → What polyskill is, in one paragraph → The five operations → 1. Bootstrap a new portable skill → 2. Import an existing runtime-specific skill → 3. Build for all configured runtimes → 4. Install into the runtime's well-known directory → 5. Inspect, validate, reconcile → Typical end-to-end flows |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 6,816 chars |

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
