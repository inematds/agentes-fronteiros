---
type: Skill
title: design-dna
description: Codifica UM design bonito (site, poster, carrossel, deck, motion, HQ) numa skill permanente — mede o original, debate o que é load-bearing, escreve dna.json + testes que podem FALHAR, reconstrói
  o original só a partir d…
resource: file:///home/nmaldaner/.claude/skills/design-dna/SKILL.md
tags:
- skill
- imagens
sources:
- path: /home/nmaldaner/.claude/skills/design-dna/SKILL.md
  author: human:nei
  last_modified: '2026-08-28'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/imagens
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 4
  subpastas:
  - assets
  - references
  scripts:
  - assets/check.py
  ferramentas: []
  gatilhos:
  - transforma esse design em skill
  - codifica esse estilo
  - quero repetir esse visual sem ele degradar
  - design DNA
  - extrai o DNA visual
  - meu output tá virando slop/genérico
  tamanho_skill_md: 7887
migracao:
  estagio: inventariado
  cluster: imagens
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# design-dna

## Descrição (do SKILL.md)

Codifica UM design bonito (site, poster, carrossel, deck, motion, HQ) numa skill permanente — mede o original, debate o que é load-bearing, escreve dna.json + testes que podem FALHAR, reconstrói o original só a partir da spec, e emite uma pasta de skill reutilizável. Use quando o usuário disser "transforma esse design em skill", "codifica esse estilo", "quero repetir esse visual sem ele degradar", "design DNA", "extrai o DNA visual", "meu output tá virando slop/genérico", ou entregar uma imagem/URL/HTML pedindo o estilo preservado.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Codifica UM design bonito (site, poster, carrossel, deck, motion, HQ) numa skill permanente — mede o original, debate o que é load-bearing, escreve dna.json +… |
| Entradas (gatilhos) | transforma esse design em skill, codifica esse estilo, quero repetir esse visual sem ele degradar, design DNA, extrai o DNA visual, meu output tá virando slop/genérico |
| Ferramentas citadas | — |
| Processo (cabeçalhos) | Design DNA → O que você entrega → A decisão central: dois arquivos, não um → O que carrega a identidade (leia antes de começar) → "Never" vence "always" → O processo — 7 passos, mostre o trabalho em cada um → Testes: exemplos → Regras para você, o analista → Arquivos |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 7,887 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/check.py`

## Cluster

[imagens](../clusters/imagens.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
