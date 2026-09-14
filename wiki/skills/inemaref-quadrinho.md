---
type: Skill
title: inemaref-quadrinho
description: Monta uma PAGINA de quadrinho/manga a partir de uma HISTORIA (e, opcionalmente, da referencia.json de um personagem do folder). Gera 6 quadros textless (estilo manga p&b) e poe narracao, baloes
  de fala e SFX como camada…
resource: file:///home/nmaldaner/.claude/skills/inemaref-quadrinho/SKILL.md
tags:
- skill
- inemaref
sources:
- path: /home/nmaldaner/.claude/skills/inemaref-quadrinho/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/inemaref
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 23
  subpastas:
  - scripts
  - templates
  - tests
  scripts:
  - scripts/_deps.py
  - scripts/build_pagina.py
  - scripts/face_zones.py
  - scripts/fill_pagina.py
  - tests/test_build_pagina.py
  - tests/test_fill_pagina.py
  - tests/test_moldura_textless.py
  ferramentas:
  - flux
  - python
  gatilhos:
  - fazer quadrinho
  - pagina de manga
  - transformar a historia em HQ
  - quadrinizar
  - comic page
  tamanho_skill_md: 4158
migracao:
  estagio: inventariado
  cluster: inemaref
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# inemaref-quadrinho

## Descrição (do SKILL.md)

Monta uma PAGINA de quadrinho/manga a partir de uma HISTORIA (e, opcionalmente, da referencia.json de um personagem do folder). Gera 6 quadros textless (estilo manga p&b) e poe narracao, baloes de fala e SFX como camada por cima, renderizando pra PNG. Use quando o usuario quiser "fazer quadrinho", "pagina de manga", "transformar a historia em HQ", "quadrinizar", "comic page". Dois modelos de pagina: grade-uniforme (todos os quadros iguais) e manga-dinamico (tamanhos diferentes).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Monta uma PAGINA de quadrinho/manga a partir de uma HISTORIA (e, opcionalmente, da referencia.json de um personagem do folder). Gera 6 quadros textless (estilo… |
| Entradas (gatilhos) | fazer quadrinho, pagina de manga, transformar a historia em HQ, quadrinizar, comic page |
| Ferramentas citadas | flux, python |
| Processo (cabeçalhos) | Skill: quadrinho — pagina de HQ/manga (passo 2 do inemaref) → Entrada → Passos → Modelos de pagina → Arte / motor → Moldura, kicker e saidas → Help |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts, templates, tests · SKILL.md com 4,158 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/_deps.py`
- `scripts/build_pagina.py`
- `scripts/face_zones.py`
- `scripts/fill_pagina.py`
- `tests/test_build_pagina.py`
- `tests/test_fill_pagina.py`
- `tests/test_moldura_textless.py`

## Cluster

[inemaref](../clusters/inemaref.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
