---
type: Skill
title: inemaref-serie
description: Cria uma SERIE completa a partir de um ASSUNTO — escreve a BIBLIA (premissa, protagonista com folder, elenco, estilo, outline de episodios), e apos aprovacao gera todos os EPISODIOS e suas
  paginas em texto / HQ / video,…
resource: file:///home/nmaldaner/.claude/skills/inemaref-serie/SKILL.md
tags:
- skill
- inemaref
sources:
- path: /home/nmaldaner/.claude/skills/inemaref-serie/SKILL.md
  author: human:nei
  last_modified: '2026-06-28'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/inemaref
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 53
  subpastas:
  - scripts
  - tests
  scripts:
  - scripts/_deps.py
  - scripts/biblia.py
  - scripts/build_serie.py
  - scripts/casting.py
  - scripts/config.py
  - scripts/lint_paineis.py
  - scripts/manifesto.py
  - scripts/naming.py
  - scripts/referencia_ep.py
  - scripts/revisar_acentos.py
  - scripts/runner.py
  - tests/test_ancoras_autoload.py
  - tests/test_biblia.py
  - tests/test_build_serie.py
  - tests/test_casting.py
  - tests/test_config.py
  - tests/test_destino.py
  - tests/test_lint_paineis.py
  - tests/test_manifesto.py
  - tests/test_naming.py
  - tests/test_referencia_ep.py
  - tests/test_revisar_acentos.py
  - tests/test_runner.py
  ferramentas:
  - ffmpeg
  - inemavox
  - pixflow
  - python
  - tts
  gatilhos:
  - criar uma serie
  - transformar um assunto numa serie
  - episodios de um canal
  - biblia da serie
  - serie de quadrinhos/HQ/video sobre X
  tamanho_skill_md: 9528
migracao:
  estagio: inventariado
  cluster: inemaref
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# inemaref-serie

## Descrição (do SKILL.md)

Cria uma SERIE completa a partir de um ASSUNTO — escreve a BIBLIA (premissa, protagonista com folder, elenco, estilo, outline de episodios), e apos aprovacao gera todos os EPISODIOS e suas paginas em texto / HQ / video, reusando folder, quadrinho e motioncomic, largando os arquivos nomeados + manifesto.json numa pasta de destino. Use quando o usuario quiser "criar uma serie", "transformar um assunto numa serie", "episodios de um canal", "biblia da serie", "serie de quadrinhos/HQ/video sobre X". Portao de aprovacao na biblia (flag auto pula). V2 do inemaref.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Cria uma SERIE completa a partir de um ASSUNTO — escreve a BIBLIA (premissa, protagonista com folder, elenco, estilo, outline de episodios), e apos aprovacao g… |
| Entradas (gatilhos) | criar uma serie, transformar um assunto numa serie, episodios de um canal, biblia da serie, serie de quadrinhos/HQ/video sobre X |
| Ferramentas citadas | ffmpeg, inemavox, pixflow, python, tts |
| Processo (cabeçalhos) | Skill: serie — criador de serie ponta a ponta (passo 4 do inemaref) → Entrada → Passo 1 — escreva a biblia → Passo 2 — pacote de aprovacao → Passo 3 — roteiros dos episodios → Coerencia por episodio (variacoes + QC) → Passo 4 — rode o lote → Pre-requisitos → Tipos -> entrega → Estilo — moldura e cor_destaque |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts, tests · SKILL.md com 9,528 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/_deps.py`
- `scripts/biblia.py`
- `scripts/build_serie.py`
- `scripts/casting.py`
- `scripts/config.py`
- `scripts/lint_paineis.py`
- `scripts/manifesto.py`
- `scripts/naming.py`
- `scripts/referencia_ep.py`
- `scripts/revisar_acentos.py`
- `scripts/runner.py`
- `tests/test_ancoras_autoload.py`
- `tests/test_biblia.py`
- `tests/test_build_serie.py`
- `tests/test_casting.py`
- `tests/test_config.py`
- `tests/test_destino.py`
- `tests/test_lint_paineis.py`
- `tests/test_manifesto.py`
- `tests/test_naming.py`
- `tests/test_referencia_ep.py`
- `tests/test_revisar_acentos.py`
- `tests/test_runner.py`

## Cluster

[inemaref](../clusters/inemaref.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
