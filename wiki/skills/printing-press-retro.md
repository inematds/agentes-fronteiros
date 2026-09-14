---
type: Skill
title: printing-press-retro
description: Run a retrospective after generating a CLI. Identifies systemic improvements to the Printing Press — templates, Go binary, skill instructions, catalog — so the next CLI comes out better. Creates
  a GitHub issue with acti…
resource: file:///home/nmaldaner/.claude/skills/printing-press-retro/SKILL.md
tags:
- skill
- printing-press
sources:
- path: /home/nmaldaner/.claude/skills/printing-press-retro/SKILL.md
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
  arquivos: 4
  subpastas:
  - references
  scripts: []
  ferramentas:
  - github
  gatilhos:
  - retro
  - retrospective
  - what went wrong
  - improve the press
  - post-mortem
  - lessons learned
  - what can we improve
  - file a retro
  - submit findings
  tamanho_skill_md: 45030
migracao:
  estagio: inventariado
  cluster: printing-press
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# printing-press-retro

## Descrição (do SKILL.md)

Run a retrospective after generating a CLI. Identifies systemic improvements to the Printing Press — templates, Go binary, skill instructions, catalog — so the next CLI comes out better. Creates a GitHub issue with actionable findings when there are Printing Press fixes to make. Use after any /printing-press run. Trigger phrases: "retro", "retrospective", "what went wrong", "improve the press", "post-mortem", "lessons learned", "what can we improve", "file a retro", "submit findings".


## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Run a retrospective after generating a CLI. Identifies systemic improvements to the Printing Press — templates, Go binary, skill instructions, catalog — so the… |
| Entradas (gatilhos) | retro, retrospective, what went wrong, improve the press, post-mortem, lessons learned, what can we improve, file a retro, submit findings |
| Ferramentas citadas | github |
| Processo (cabeçalhos) | /printing-press-retro → Terminology → Cardinal rules → Setup → Path-only setup — no binary detection required. → The retro skill reads manuscripts and runs gh/curl. It does not invoke the → printing-press binary. This avoids aborting for users who installed the → plugin but not the Go binary. → Detect whether we're inside the printing-press repo → Guard rails |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references · SKILL.md com 45,030 chars |

## Cluster

[printing-press](../clusters/printing-press.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
