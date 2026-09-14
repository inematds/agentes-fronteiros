---
type: Skill
title: printing-press-output-review
description: 'Internal sub-skill: agentic review of a printed CLI''s sampled command output for plausibility issues that rule-based checks can''t encode (substring-match relevance, format bugs, silent source
  drops, ranking failures). I…'
resource: file:///home/nmaldaner/.claude/skills/printing-press-output-review/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-output-review/SKILL.md
  author: human:nei
  last_modified: '2026-05-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/printing-press
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas: []
  gatilhos: []
  tamanho_skill_md: 9303
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-output-review

## Descrição (do SKILL.md)

Internal sub-skill: agentic review of a printed CLI's sampled command output for plausibility issues that rule-based checks can't encode (substring-match relevance, format bugs, silent source drops, ranking failures). Invoked via the Skill tool by main printing-press SKILL.md (Phase 4.85) and printing-press-polish SKILL.md during the diagnostic loop. Not for direct user invocation — its actionable wrappers are /printing-press and /printing-press-polish.


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Internal sub-skill: agentic review of a printed CLI's sampled command output for plausibility issues that rule-based checks can't encode (substring-match relev… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | — |
| Processo (cabeçalhos) | printing-press-output-review (internal) → Input → What this catches → Procedure → Step 1: Gather sample data → Locate research.json. Adjacent to the binary covers the post-promote → layout (standalone polish, shipcheck against the library copy). The → grandparent fallback covers mid-pipeline invocations where $CLI_DIR is → $PRESS_RUNSTATE/runs/<id>/working/<cli> and research.json lives at → $PRESS_RUNSTATE/runs/<id>/research.json. Without the fallback, scorecard |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 9,303 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
