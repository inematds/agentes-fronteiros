---
type: Skill
title: fable-mindset
description: ''
resource: file:///home/nmaldaner/.claude/skills/fable-mindset/SKILL.md
tags:
- skill
- conselho
sources:
- path: /home/nmaldaner/.claude/skills/fable-mindset/SKILL.md
  author: human:nei
  last_modified: '2026-06-16'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/conselho
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 10
  subpastas:
  - scripts
  scripts:
  - scripts/compare_models.py
  - scripts/debloat_jsonl.py
  - scripts/extract_corpus.py
  - scripts/fable_lib.py
  - scripts/import_hf_traces.py
  - scripts/make_playbook.py
  ferramentas:
  - python
  gatilhos: []
  tamanho_skill_md: 8351
migracao:
  estagio: inventariado
  cluster: conselho
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# fable-mindset

## Descrição (do SKILL.md)

_sem descrição_

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | — |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | python |
| Processo (cabeçalhos) | Fable Mindset → Conceito-chave: TURNO LÓGICO → Achado honesto: raciocínio cifrado → O pipeline em 5 passos → 1) DEBLOAT — destila 1 sessão numa transcrição leve (remove tool_results, dumps, → anexos; ~74% menor). Útil para LER uma sessão antes de minerar tudo. → 2) LISTAR MODELOS — quais modelos existem no SEU histórico e quantos turnos cada um. → 3) EXTRAIR CORPUS — pega TODOS os turnos de 1 modelo de todo o histórico → (escreve transcript.md + stats.json) e imprime os números medidos. → 4) COMPARAR — 2 modelos lado a lado: o delta de ritmo. Salve o compare.json. |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts · SKILL.md com 8,351 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/compare_models.py`
- `scripts/debloat_jsonl.py`
- `scripts/extract_corpus.py`
- `scripts/fable_lib.py`
- `scripts/import_hf_traces.py`
- `scripts/make_playbook.py`

## Cluster

[conselho](../clusters/conselho.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
