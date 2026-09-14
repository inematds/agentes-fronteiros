---
type: Skill
title: comfy-deploy
description: Run a Comfy Build release as a serverless deployment with comfy-cli. Use whenever the user wants to deploy, serve, host, or expose a ComfyUI build as an endpoint, scale or stop workers, submit
  a workflow to a deployment…
resource: file:///home/nmaldaner/.claude/skills/comfy-deploy/SKILL.md
tags:
- skill
- comfy
sources:
- path: /home/nmaldaner/.claude/skills/comfy-deploy/SKILL.md
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
  - github
  - node
  gatilhos: []
  tamanho_skill_md: 15646
migracao:
  estagio: inventariado
  cluster: comfy
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# comfy-deploy

## Descrição (do SKILL.md)

Run a Comfy Build release as a serverless deployment with comfy-cli. Use whenever the user wants to deploy, serve, host, or expose a ComfyUI build as an endpoint, scale or stop workers, submit a workflow to a deployment, check whether a deployment is healthy or running a stale release, or work out why one is still costing money. Covers `comfy deploy up / run / status / scale / stop / start / delete / ls / show / logs / events / refs`. Assumes a green release already exists — `comfy-build` is the skill that produces one.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Run a Comfy Build release as a serverless deployment with comfy-cli. Use whenever the user wants to deploy, serve, host, or expose a ComfyUI build as an endpoi… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | comfyui, github, node |
| Processo (cabeçalhos) | comfy-deploy → What you are working with → The command surface → The path → The cost model, which is the whole risk → Deployment states → `comfy deploy up` → `comfy deploy run` → Reading a deployment → Giving compute back |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 15,646 chars |

## Cluster

[comfy](../clusters/comfy.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
