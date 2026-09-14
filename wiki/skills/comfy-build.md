---
type: Skill
title: comfy-build
description: 'Build a custom ComfyUI environment on the Comfy developer platform with comfy-cli: turn a local install, a ComfyUI Desktop snapshot, a workflow JSON, or nothing but a Dockerfile, a Modal script
  or a sentence into a comm…'
resource: file:///home/nmaldaner/.claude/skills/comfy-build/SKILL.md
tags:
- skill
- comfy
sources:
- path: /home/nmaldaner/.claude/skills/comfy-build/SKILL.md
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
  - python
  gatilhos: []
  tamanho_skill_md: 17172
migracao:
  estagio: inventariado
  cluster: comfy
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# comfy-build

## Descrição (do SKILL.md)

Build a custom ComfyUI environment on the Comfy developer platform with comfy-cli: turn a local install, a ComfyUI Desktop snapshot, a workflow JSON, or nothing but a Dockerfile, a Modal script or a sentence into a committed comfy-build.yaml and a green release. Use whenever the user wants to package, build, pin, or reproduce a ComfyUI environment, decide the dependency pins before the first cut, or read a failed build's log. Stops at a green release; comfy-deploy takes it from there.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Build a custom ComfyUI environment on the Comfy developer platform with comfy-cli: turn a local install, a ComfyUI Desktop snapshot, a workflow JSON, or nothin… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | comfyui, github, node, python |
| Processo (cabeçalhos) | comfy-build → What the platform is → The command surface → Depth, on demand → Which path you are on → Path A — from a ComfyUI install → Path A′ — the Desktop snapshot → Path B — from a workflow file → Path C — from a description, a Dockerfile, or a Modal script → What the CLI decides, so you do not |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 17,172 chars |

## Cluster

[comfy](../clusters/comfy.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
