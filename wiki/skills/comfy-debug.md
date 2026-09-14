---
type: Skill
title: comfy-debug
description: Debugging skill for the comfy CLI — failed workflows, stuck jobs, error envelopes, and the fastest path from "it broke" to "fixed".
resource: file:///home/nmaldaner/.claude/skills/comfy-debug/SKILL.md
tags:
- skill
- comfy
sources:
- path: /home/nmaldaner/.claude/skills/comfy-debug/SKILL.md
  author: human:nei
  last_modified: '2026-09-02'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/comfy
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - comfyui
  - node
  - python
  gatilhos:
  - it broke
  - fixed
  tamanho_skill_md: 9248
migracao:
  estagio: inventariado
  cluster: comfy
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# comfy-debug

## Descrição (do SKILL.md)

Debugging skill for the comfy CLI — failed workflows, stuck jobs, error envelopes, and the fastest path from "it broke" to "fixed".

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Debugging skill for the comfy CLI — failed workflows, stuck jobs, error envelopes, and the fastest path from "it broke" to "fixed". |
| Entradas (gatilhos) | it broke, fixed |
| Ferramentas citadas | comfyui, node, python |
| Processo (cabeçalhos) | The envelope is the source of truth → Decision tree for common failures → `server_not_running` (local) → or, for background mode: → `cloud_not_configured` / `cloud_unauthorized` (cloud) → or, if you already have an API key: → `transient_auth` (cloud job failed with "Unauthorized: Please login first to use this node") → `workflow_not_api_format` → `workflow_invalid_json` → `prompt_rejected` (server returned `node_errors`) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 9,248 chars |

## Cluster

[comfy](../clusters/comfy.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
