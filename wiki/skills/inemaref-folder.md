---
type: Skill
title: inemaref-folder
description: Cria a FICHA DE REFERENCIA (model sheet) de um personagem a partir de uma FOTO (pessoa real) ou de um TEXTO (descricao/historia). Saida = pagina editorial (folder.png) + folder.html editavel
  + assets/ (imagens cruas) +…
resource: file:///home/nmaldaner/.claude/skills/inemaref-folder/SKILL.md
tags:
- skill
- inemaref
sources:
- path: /home/nmaldaner/.claude/skills/inemaref-folder/SKILL.md
  author: human:nei
  last_modified: '2026-06-11'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/inemaref
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 45
  subpastas:
  - scripts
  - templates
  - tests
  scripts:
  - scripts/_deps.py
  - scripts/artes.py
  - scripts/build_folder.py
  - scripts/fill_template.py
  - scripts/imgclient.py
  - scripts/png_size.py
  - scripts/qc_imagem.py
  - scripts/referencia.py
  - scripts/render.py
  - tests/test_artes.py
  - tests/test_build_folder.py
  - tests/test_dossie_fill.py
  - tests/test_fill_template.py
  - tests/test_imgclient.py
  - tests/test_png_size.py
  - tests/test_qc_imagem.py
  - tests/test_referencia.py
  - tests/test_render.py
  ferramentas:
  - flux
  - python
  gatilhos:
  - criar referencia
  - ficha de personagem
  - model sheet
  - folder do personagem
  tamanho_skill_md: 3621
migracao:
  estagio: inventariado
  cluster: inemaref
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# inemaref-folder

## Descrição (do SKILL.md)

Cria a FICHA DE REFERENCIA (model sheet) de um personagem a partir de uma FOTO (pessoa real) ou de um TEXTO (descricao/historia). Saida = pagina editorial (folder.png) + folder.html editavel + assets/ (imagens cruas) + referencia.json travado. Use quando o usuario quiser "criar referencia", "ficha de personagem", "model sheet", "folder do personagem", ou der uma foto/historia e pedir a pagina de referencia do inemaref. Dois layouts (editorial-revista, dossie) x duas artes (foto, cartoon), combinaveis.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Cria a FICHA DE REFERENCIA (model sheet) de um personagem a partir de uma FOTO (pessoa real) ou de um TEXTO (descricao/historia). Saida = pagina editorial (fol… |
| Entradas (gatilhos) | criar referencia, ficha de personagem, model sheet, folder do personagem |
| Ferramentas citadas | flux, python |
| Processo (cabeçalhos) | Skill: folder — ficha de referencia (passo 0 do inemaref) → Entrada → Passos → Estilos → Motor de imagem → Help |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts, templates, tests · SKILL.md com 3,621 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/_deps.py`
- `scripts/artes.py`
- `scripts/build_folder.py`
- `scripts/fill_template.py`
- `scripts/imgclient.py`
- `scripts/png_size.py`
- `scripts/qc_imagem.py`
- `scripts/referencia.py`
- `scripts/render.py`
- `tests/test_artes.py`
- `tests/test_build_folder.py`
- `tests/test_dossie_fill.py`
- `tests/test_fill_template.py`
- `tests/test_imgclient.py`
- `tests/test_png_size.py`
- `tests/test_qc_imagem.py`
- `tests/test_referencia.py`
- `tests/test_render.py`

## Cluster

[inemaref](../clusters/inemaref.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
