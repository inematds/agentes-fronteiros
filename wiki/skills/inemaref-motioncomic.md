---
type: Skill
title: inemaref-motioncomic
description: Transforma uma HISTORIA em quadros num VIDEO de motion comic (16:9) — a camera da ZOOM em cada quadro durante a sua narracao (push-in), com voz (TTS inemavox) e balao/SFX como camada. Use quando
  o usuario quiser "video…
resource: file:///home/nmaldaner/.claude/skills/inemaref-motioncomic/SKILL.md
tags:
- skill
- inemaref
sources:
- path: /home/nmaldaner/.claude/skills/inemaref-motioncomic/SKILL.md
  author: human:nei
  last_modified: '2026-06-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/inemaref
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 43
  subpastas:
  - scripts
  - tests
  scripts:
  - scripts/_deps.py
  - scripts/build_motion.py
  - scripts/build_travel.py
  - scripts/forma_c.py
  - scripts/forma_c_direcao.py
  - scripts/overlay.py
  - scripts/tts.py
  - scripts/visao_decupagem.py
  - tests/test_forma_c.py
  - tests/test_forma_c_direcao.py
  - tests/test_motion.py
  - tests/test_preset_visao.py
  - tests/test_seq_visao.py
  - tests/test_textless_path.py
  - tests/test_travel.py
  - tests/test_tts_revisao.py
  - tests/test_visao_decupagem.py
  ferramentas:
  - ffmpeg
  - flux
  - inemavox
  - pixflow
  - python
  - tts
  gatilhos:
  - video de quadrinhos
  - motion comic
  - quadrinho narrado em video
  - dar zoom no quadro quando narra
  - transformar a HQ em video
  - camera viajando sobre a pagina
  tamanho_skill_md: 9147
migracao:
  estagio: inventariado
  cluster: inemaref
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# inemaref-motioncomic

## Descrição (do SKILL.md)

Transforma uma HISTORIA em quadros num VIDEO de motion comic (16:9) — a camera da ZOOM em cada quadro durante a sua narracao (push-in), com voz (TTS inemavox) e balao/SFX como camada. Use quando o usuario quiser "video de quadrinhos", "motion comic", "quadrinho narrado em video", "dar zoom no quadro quando narra", "transformar a HQ em video", "camera viajando sobre a pagina". Arte cartoon/manga, narracao voz-off, balao so com fala/expressao.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Transforma uma HISTORIA em quadros num VIDEO de motion comic (16:9) — a camera da ZOOM em cada quadro durante a sua narracao (push-in), com voz (TTS inemavox)… |
| Entradas (gatilhos) | video de quadrinhos, motion comic, quadrinho narrado em video, dar zoom no quadro quando narra, transformar a HQ em video, camera viajando sobre a pagina |
| Ferramentas citadas | ffmpeg, flux, inemavox, pixflow, python, tts |
| Processo (cabeçalhos) | Skill: motioncomic — quadrinho em video com zoom (passo 3 do inemaref) → Duas formas → Como funciona (pipeline) → Entrada — o roteiro → Rodar → Ajustes (Forma B) → Narracao — revisao de escrita + pronuncia (antes do TTS) → Forma C — filme dirigido dos paineis (acao) → Help |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: scripts, tests · SKILL.md com 9,147 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/_deps.py`
- `scripts/build_motion.py`
- `scripts/build_travel.py`
- `scripts/forma_c.py`
- `scripts/forma_c_direcao.py`
- `scripts/overlay.py`
- `scripts/tts.py`
- `scripts/visao_decupagem.py`
- `tests/test_forma_c.py`
- `tests/test_forma_c_direcao.py`
- `tests/test_motion.py`
- `tests/test_preset_visao.py`
- `tests/test_seq_visao.py`
- `tests/test_textless_path.py`
- `tests/test_travel.py`
- `tests/test_tts_revisao.py`
- `tests/test_visao_decupagem.py`

## Cluster

[inemaref](../clusters/inemaref.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
