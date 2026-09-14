---
type: Skill
title: atualiza-portal
description: 'Publica curso ou projeto (URL github.io) nas 3 superfícies INEMA — portal (inema.club), inemabuscas e catálogo PRO — com commit e push nos 3 repos. Gatilho: "coloca/publica/adiciona no portal",
  ou a URL do item.'
resource: file:///home/nmaldaner/.claude/skills/atualiza-portal/SKILL.md
tags:
- skill
- publicacao
sources:
- path: /home/nmaldaner/.claude/skills/atualiza-portal/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:32:36Z'
status: draft
related:
- clusters/publicacao
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas:
  - scripts
  scripts:
  - scripts/publica.sh
  ferramentas:
  - flux
  - github
  - node
  - supabase
  - telegram
  - vercel
  gatilhos:
  - coloca/publica/adiciona no portal
  tamanho_skill_md: 20331
migracao:
  estagio: inventariado
  cluster: publicacao
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# atualiza-portal

## Descrição (do SKILL.md)

Publica curso ou projeto (URL github.io) nas 3 superfícies INEMA — portal (inema.club), inemabuscas e catálogo PRO — com commit e push nos 3 repos. Gatilho: "coloca/publica/adiciona no portal", ou a URL do item.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Publica curso ou projeto (URL github.io) nas 3 superfícies INEMA — portal (inema.club), inemabuscas e catálogo PRO — com commit e push nos 3 repos. Gatilho: "c… |
| Entradas (gatilhos) | coloca/publica/adiciona no portal |
| Ferramentas citadas | flux, github, node, supabase, telegram, vercel |
| Processo (cabeçalhos) | atualiza-portal → O que a home ainda mostra (mudança de 2026-08-01) → Por que 3 repos → Caminhos fixos → Os arrays: curso em `courses.ts`, projeto em `Portal.tsx` → Shapes (dos próprios arquivos) → Trilhas (cursos) → Procedimento → 0. Garantir a URL de destino — gerar o guia se faltar (projeto sem guia) → 1. Extrair os metadados da URL |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 20,331 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/publica.sh`

## Cluster

[publicacao](../clusters/publicacao.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
