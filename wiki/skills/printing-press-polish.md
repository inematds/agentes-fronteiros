---
type: Skill
title: printing-press-polish
description: Polish a generated CLI to pass verification and become publish-ready. Runs diagnostics (dogfood, verify, scorecard, go vet), automatically fixes all issues (verify failures, dead code, descriptions,
  README, MCP tool qua…
resource: file:///home/nmaldaner/.claude/skills/printing-press-polish/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-polish/SKILL.md
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
  arquivos: 3
  subpastas:
  - references
  scripts: []
  ferramentas:
  - github
  - mcp
  gatilhos:
  - polish
  - improve the CLI
  - fix verify
  - make it publish-ready
  - clean up the CLI
  - get this ready to ship
  tamanho_skill_md: 54919
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-polish

## Descrição (do SKILL.md)

Polish a generated CLI to pass verification and become publish-ready. Runs diagnostics (dogfood, verify, scorecard, go vet), automatically fixes all issues (verify failures, dead code, descriptions, README, MCP tool quality), reports the before/after delta, and offers to publish. Use after any /printing-press run, or on any CLI in ~/printing-press/library/. Trigger phrases: "polish", "improve the CLI", "fix verify", "make it publish-ready", "clean up the CLI", "get this ready to ship".


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Polish a generated CLI to pass verification and become publish-ready. Runs diagnostics (dogfood, verify, scorecard, go vet), automatically fixes all issues (ve… |
| Entradas (gatilhos) | polish, improve the CLI, fix verify, make it publish-ready, clean up the CLI, get this ready to ship |
| Ferramentas citadas | github, mcp |
| Processo (cabeçalhos) | /printing-press-polish → When to run → Setup → min-binary-version: 4.0.0 → Public-library hint → Resolve CLI → Check if there's an active build lock — polish edits would be overwritten → when the running build promotes to library. → Verify it's a valid Go CLI → Find spec and research dir |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 54,919 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
