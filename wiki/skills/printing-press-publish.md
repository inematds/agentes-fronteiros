---
type: Skill
title: printing-press-publish
description: Publish a generated CLI to the printing-press-library repo
resource: file:///home/nmaldaner/.claude/skills/printing-press-publish/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-publish/SKILL.md
  author: human:nei
  last_modified: '2026-05-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/printing-press
skill:
  versao: 0.1.0
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - github
  - mcp
  gatilhos: []
  tamanho_skill_md: 43075
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-publish

## Descrição (do SKILL.md)

Publish a generated CLI to the printing-press-library repo

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Publish a generated CLI to the printing-press-library repo |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | github, mcp |
| Processo (cabeçalhos) | /printing-press publish → Setup → min-binary-version: 4.0.0 → Derive scope first — needed for local build detection → Prefer local build when running from inside the printing-press repo. → Configuration → Publish config → Scoped clone cleanup → Step 1: Prerequisites → Step 2: Resolve API Slug |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 43,075 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
