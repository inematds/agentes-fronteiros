---
type: Skill
title: formato-curso-v4
description: curso INEMA v4 — PÁGINA ÚNICA (trilha + aulas como views, roteamento por hash), dark editorial COM movimento (cold-open que fisga + corpo de leitura calmo com trilho vivo na margem) e camada
  de aprendizagem nível 3 com…
resource: file:///home/nmaldaner/.claude/skills/formato-curso-v4/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/formato-curso-v4/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/curso
skill:
  versao: ''
  invocacao_pelo_modelo: false
  arquivos: 5
  subpastas:
  - assets
  - references
  scripts:
  - assets/curso.js
  ferramentas:
  - github
  - node
  gatilhos:
  - pratique agora / mão na massa
  - explique com suas palavras
  - minha jornada
  - página única
  - formato de curso v4
  tamanho_skill_md: 11036
migracao:
  estagio: inventariado
  cluster: curso
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# formato-curso-v4

## Descrição (do SKILL.md)

curso INEMA v4 — PÁGINA ÚNICA (trilha + aulas como views, roteamento por hash), dark editorial COM movimento (cold-open que fisga + corpo de leitura calmo com trilho vivo na margem) e camada de aprendizagem nível 3 com RETENÇÃO. Self-contained, offline, um só estado em localStorage. Use SEMPRE que o usuário pedir para criar, editar ou revisar um curso HTML no estilo v4 — landing, trilha ou aula — e ao mencionar "pratique agora / mão na massa", reflexão/"explique com suas palavras", flashcards do grifo, revisão espaçada, "minha jornada", teste-se com feedback, mapa da aula, preferências de leitura (Aa), glossário, onboarding, temas dark/papel/sépia, "página única", "formato de curso v4". Rompe com o v1/v2 (dark âmbar) e com o papel-first do v3, costurando os dois.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | curso INEMA v4 — PÁGINA ÚNICA (trilha + aulas como views, roteamento por hash), dark editorial COM movimento (cold-open que fisga + corpo de leitura calmo com… |
| Entradas (gatilhos) | pratique agora / mão na massa, explique com suas palavras, minha jornada, página única, formato de curso v4 |
| Ferramentas citadas | github, node |
| Processo (cabeçalhos) | Formato Curso v4 — INEMA (página única, dark editorial com retenção) → Referência obrigatória → Por que PÁGINA ÚNICA (constraint que definiu a arquitetura) → Os dois assets (assets/) — o que é AUTOMÁTICO vs AUTORADO → Contrato de markup (o que VOCÊ escreve) → Esqueleto do documento → Barra (chrome global, estática) → View da trilha — `<section class="view" id="v-trilha">` → Views de aula — `<section class="view" id="v-aula-N" data-aula="N">` → Teste-se (quiz) — dentro de um step |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 11,036 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/curso.js`

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
