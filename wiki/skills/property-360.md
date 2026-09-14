---
type: Skill
title: property-360
description: Transforma várias fotos comuns de um MESMO cômodo (ou só uma descrição em texto) numa panorâmica 360° equiretangular 2:1 (4096×2048) fotorrealista, fiel ao imóvel, com checagem de proporção
  e costura e viewer 360. Use q…
resource: file:///home/nmaldaner/.claude/skills/property-360/SKILL.md
tags:
- skill
- publicacao
sources:
- path: /home/nmaldaner/.claude/skills/property-360/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/publicacao
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - flux
  - gemini
  - magnific
  - python
  gatilhos:
  - 360 da sala
  - panorâmica do cômodo
  - tour virtual a partir de fotos
  - vira 360
  - property 360
  tamanho_skill_md: 2609
migracao:
  estagio: inventariado
  cluster: publicacao
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# property-360

## Descrição (do SKILL.md)

Transforma várias fotos comuns de um MESMO cômodo (ou só uma descrição em texto) numa panorâmica 360° equiretangular 2:1 (4096×2048) fotorrealista, fiel ao imóvel, com checagem de proporção e costura e viewer 360. Use quando o usuário pedir "360 da sala", "panorâmica do cômodo", "tour virtual a partir de fotos", "vira 360", "property 360", ou der uma pasta de fotos de um ambiente / um assunto de cômodo e quiser a imagem 360.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Transforma várias fotos comuns de um MESMO cômodo (ou só uma descrição em texto) numa panorâmica 360° equiretangular 2:1 (4096×2048) fotorrealista, fiel ao imó… |
| Entradas (gatilhos) | 360 da sala, panorâmica do cômodo, tour virtual a partir de fotos, vira 360, property 360 |
| Ferramentas citadas | flux, gemini, magnific, python |
| Processo (cabeçalhos) | property-360 — fotos comuns → sala em 360° → Fluxo (o script faz tudo; você orquestra e revisa) → Modelos → Regras |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 2,609 chars |

## Cluster

[publicacao](../clusters/publicacao.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
