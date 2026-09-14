---
type: Skill
title: maestro-roteador
description: Use when despachando trabalho para subagentes/workflows, quando o usuário passa um problema e pergunta qual modelo ou esforço usar, ou antes de escolher model/effort em qualquer chamada Agent/Workflow.
  Gatilhos - "qual…
resource: file:///home/nmaldaner/.claude/skills/maestro-roteador/SKILL.md
tags:
- skill
- conselho
sources:
- path: /home/nmaldaner/.claude/skills/maestro-roteador/SKILL.md
  author: human:nei
  last_modified: '2026-07-15'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/conselho
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 2
  subpastas: []
  scripts: []
  ferramentas: []
  gatilhos:
  - qual modelo
  - quanto esforço
  - triagem
  - faz a triagem disso
  tamanho_skill_md: 7272
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# maestro-roteador

## Descrição (do SKILL.md)

Use when despachando trabalho para subagentes/workflows, quando o usuário passa um problema e pergunta qual modelo ou esforço usar, ou antes de escolher model/effort em qualquer chamada Agent/Workflow. Gatilhos - "qual modelo", "quanto esforço", "triagem", "faz a triagem disso", pedidos brutos que precisam ser distribuídos.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Use when despachando trabalho para subagentes/workflows, quando o usuário passa um problema e pergunta qual modelo ou esforço usar, ou antes de escolher model/… |
| Entradas (gatilhos) | qual modelo, quanto esforço, triagem, faz a triagem disso |
| Ferramentas citadas | — |
| Processo (cabeçalhos) | Maestro Roteador — seleção de modelo e esforço → Princípio central → Procedimento (sempre nesta ordem) → Tabela rápida → Armadilhas (vistas em teste real) → Anti-overhead: a triagem também tem custo → Cache: o custo escondido da troca de modelo → Empate de gosto → oferece a escolha (custo × qualidade) → Formato de saída (plano de despacho) → Limite |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 7,272 chars |

## Cluster

[conselho](../clusters/conselho.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
