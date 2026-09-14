---
type: Skill
title: clima
description: Clima atual e previsão (até 16 dias) de qualquer cidade via Open-Meteo, sem API key, em PT-BR. Vale também para decisões que dependem do tempo ("posso gravar externa amanhã?", "levo guarda-chuva?").
  Não cobre clima hist…
resource: file:///home/nmaldaner/.claude/skills/clima/SKILL.md
tags:
- skill
- pesquisa-web
sources:
- path: /home/nmaldaner/.claude/skills/clima/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/pesquisa-web
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 3
  subpastas:
  - evals
  - scripts
  scripts:
  - scripts/clima.mjs
  ferramentas:
  - node
  gatilhos:
  - posso gravar externa amanhã?
  - levo guarda-chuva?
  tamanho_skill_md: 5690
migracao:
  estagio: inventariado
  cluster: pesquisa-web
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# clima

## Descrição (do SKILL.md)

Clima atual e previsão (até 16 dias) de qualquer cidade via Open-Meteo, sem API key, em PT-BR. Vale também para decisões que dependem do tempo ("posso gravar externa amanhã?", "levo guarda-chuva?"). Não cobre clima histórico nem climatologia de pesquisa.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Clima atual e previsão (até 16 dias) de qualquer cidade via Open-Meteo, sem API key, em PT-BR. Vale também para decisões que dependem do tempo ("posso gravar e… |
| Entradas (gatilhos) | posso gravar externa amanhã?, levo guarda-chuva? |
| Ferramentas citadas | node |
| Processo (cabeçalhos) | Clima → O script → Qual cidade usar → Como responder → Exemplos → Limites que valem dizer |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: evals, scripts · SKILL.md com 5,690 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/clima.mjs`

## Cluster

[pesquisa-web](../clusters/pesquisa-web.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
