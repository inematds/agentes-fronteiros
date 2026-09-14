---
type: Skill
title: printing-press-reprint
description: Regenerate an existing printed CLI from scratch under the current Printing Press, with prior research and prior novel features carried into the novel-features subagent's reprint reconciliation
  rather than dropped on the…
resource: file:///home/nmaldaner/.claude/skills/printing-press-reprint/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-reprint/SKILL.md
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
  ferramentas:
  - mcp
  - python
  gatilhos:
  - reprint <api>
  - regenerate <api>
  - redo the <api> CLI
  - rebuild <api> from scratch
  - this CLI would benefit from a reprint
  tamanho_skill_md: 7573
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-reprint

## Descrição (do SKILL.md)

Regenerate an existing printed CLI from scratch under the current Printing Press, with prior research and prior novel features carried into the novel-features subagent's reprint reconciliation rather than dropped on the floor. Pulls the CLI from the public library if it isn't local, recommends reuse-vs-redo of prior research based on age, then hands off to /printing-press with the right context. Use when a machine upgrade would benefit a published CLI more than manual polish. Trigger phrases: "reprint <api>", "regenerate <api>", "redo the <api> CLI", "rebuild <api> from scratch", "this CLI would benefit from a reprint".


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Regenerate an existing printed CLI from scratch under the current Printing Press, with prior research and prior novel features carried into the novel-features… |
| Entradas (gatilhos) | reprint <api>, regenerate <api>, redo the <api> CLI, rebuild <api> from scratch, this CLI would benefit from a reprint |
| Ferramentas citadas | mcp, python |
| Processo (cabeçalhos) | /printing-press-reprint → When to run → Setup → Phase A — Resolve and reconcile presence → Phase B — Verify prior research is reconcilable → Phase C — Recency recommendation → Phase D — Hand off to `/printing-press` → After hand-off |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 7,573 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
