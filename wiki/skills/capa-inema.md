---
type: Skill
title: capa-inema
description: Gera a capa oficial INEMA (1280x720) de um repo de curso ou projeto — imagem por IA + faixa de título/marca — em `capa/capa.png`. Layouts split (default) e fb. Todo curso ou página de guia
  novo deve produzir a capa por…
resource: file:///home/nmaldaner/.claude/skills/capa-inema/SKILL.md
tags:
- skill
- imagens
sources:
- path: /home/nmaldaner/.claude/skills/capa-inema/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/imagens
skill:
  versao: ''
  invocacao_pelo_modelo: false
  arquivos: 182
  subpastas:
  - assets
  - node_modules
  scripts:
  - assets/rodar-capas-lote.mjs
  - fetch-debs.js
  ferramentas:
  - flux
  - node
  - playwright
  - vercel
  gatilhos: []
  tamanho_skill_md: 4628
migracao:
  estagio: inventariado
  cluster: imagens
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# capa-inema

## Descrição (do SKILL.md)

Gera a capa oficial INEMA (1280x720) de um repo de curso ou projeto — imagem por IA + faixa de título/marca — em `capa/capa.png`. Layouts split (default) e fb. Todo curso ou página de guia novo deve produzir a capa por aqui. Também roda em lote em vários repos.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Gera a capa oficial INEMA (1280x720) de um repo de curso ou projeto — imagem por IA + faixa de título/marca — em `capa/capa.png`. Layouts split (default) e fb.… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | flux, node, playwright, vercel |
| Processo (cabeçalhos) | capa-inema → Quando usar → Dois layouts → Uso → Dependências (checar antes) → Rodar em lote → Padrão visual (não mudar sem pedir) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, node_modules · SKILL.md com 4,628 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/rodar-capas-lote.mjs`
- `fetch-debs.js`

## Cluster

[imagens](../clusters/imagens.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
