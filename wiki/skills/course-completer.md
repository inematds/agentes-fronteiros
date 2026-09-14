---
type: Skill
title: course-completer
description: Complete Skilljar course lessons and quizzes. Use when user says "complete this lesson", "mark as complete", "finish this course", "skilljar", or is on an anthropic.skilljar.com page and wants
  lessons/quizzes completed.
resource: file:///home/nmaldaner/.claude/skills/course-completer/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/course-completer/SKILL.md
  author: human:nei
  last_modified: '2026-04-29'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/curso
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - mcp
  gatilhos:
  - complete this lesson
  - mark as complete
  - finish this course
  - skilljar
  tamanho_skill_md: 18614
migracao:
  estagio: inventariado
  cluster: curso
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# course-completer

## Descrição (do SKILL.md)

Complete Skilljar course lessons and quizzes. Use when user says "complete this lesson", "mark as complete", "finish this course", "skilljar", or is on an anthropic.skilljar.com page and wants lessons/quizzes completed.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Complete Skilljar course lessons and quizzes. Use when user says "complete this lesson", "mark as complete", "finish this course", "skilljar", or is on an anth… |
| Entradas (gatilhos) | complete this lesson, mark as complete, finish this course, skilljar |
| Ferramentas citadas | mcp |
| Processo (cabeçalhos) | Skilljar Course Completer → Lesson types on Skilljar → How Skilljar completion works → Text/Video lessons → Quiz lessons → Surveys → Key JavaScript globals on any Skilljar lesson page → Quiz-specific globals → DOM structure → Quiz DOM structure |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 18,614 chars |

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
