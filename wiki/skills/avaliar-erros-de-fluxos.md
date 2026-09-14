---
type: Skill
title: avaliar-erros-de-fluxos
description: Diagnostica erros e fragilidades em fluxos n8n/Make (lógica, expressões, filtros, paginação, nulos, N+1, timeouts) e propõe correções testáveis. Use ao receber um JSON de fluxo exportado ou
  um relato de falha intermiten…
resource: file:///home/nmaldaner/.claude/skills/avaliar-erros-de-fluxos/SKILL.md
tags:
- skill
- dev-tooling
sources:
- path: /home/nmaldaner/.claude/skills/avaliar-erros-de-fluxos/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/dev-tooling
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 3
  subpastas:
  - references
  scripts: []
  ferramentas:
  - flux
  - node
  - supabase
  gatilhos: []
  tamanho_skill_md: 3727
migracao:
  estagio: inventariado
  cluster: dev-tooling
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# avaliar-erros-de-fluxos

## Descrição (do SKILL.md)

Diagnostica erros e fragilidades em fluxos n8n/Make (lógica, expressões, filtros, paginação, nulos, N+1, timeouts) e propõe correções testáveis. Use ao receber um JSON de fluxo exportado ou um relato de falha intermitente.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Diagnostica erros e fragilidades em fluxos n8n/Make (lógica, expressões, filtros, paginação, nulos, N+1, timeouts) e propõe correções testáveis. Use ao receber… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | flux, node, supabase |
| Processo (cabeçalhos) | Skill: Avaliar Erros de Fluxos (n8n / automações) → Instruções → 1) Identificar o contexto do fluxo → 2) Validar filtros e condições → 3) Checar lógica de IFs e branches → 4) Verificar loops e paginação → 5) Detectar N+1 queries → 6) Verificar updates duplicados → 7) Validar expressões → 8) Tratamento de erros |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 3,727 chars |

## Cluster

[dev-tooling](../clusters/dev-tooling.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
