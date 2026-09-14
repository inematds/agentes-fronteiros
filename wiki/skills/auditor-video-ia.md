---
type: Skill
title: auditor-video-ia
description: Audita prompts, gerações e anúncios criados com IA antes de gastar mais ou publicar. Usar quando alguém disser "/auditor-video-ia", "revisa esse prompt", "audita esse vídeo", "regenero?", "dá
  pra consertar?", "controle…
resource: file:///home/nmaldaner/.claude/skills/auditor-video-ia/SKILL.md
tags:
- skill
- video-ia
sources:
- path: /home/nmaldaner/.claude/skills/auditor-video-ia/SKILL.md
  author: human:nei
  last_modified: '2026-09-06'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-ia
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 8
  subpastas:
  - assets
  - references
  - scripts
  scripts:
  - scripts/checa-prompt.py
  ferramentas:
  - python
  - seedance
  gatilhos:
  - /auditor-video-ia
  - revisa esse prompt
  - audita esse vídeo
  - regenero?
  - dá pra consertar?
  - controle de qualidade
  - preflight
  - postflight
  - deriva de identidade
  - falha de mãos/lip-sync
  - confere o CTA/produto/claims
  tamanho_skill_md: 6063
migracao:
  estagio: inventariado
  cluster: video-ia
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# auditor-video-ia

## Descrição (do SKILL.md)

Audita prompts, gerações e anúncios criados com IA antes de gastar mais ou publicar. Usar quando alguém disser "/auditor-video-ia", "revisa esse prompt", "audita esse vídeo", "regenero?", "dá pra consertar?", "controle de qualidade", "preflight", "postflight", "deriva de identidade", "falha de mãos/lip-sync", "confere o CTA/produto/claims" ou precisar decidir entre conservar, editar, estender, salvar na montagem ou regenerar. Valida a interface concreta, evidência, consentimento, transparência, custo e aprendizado do teste; não publica nem gasta crédito.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Audita prompts, gerações e anúncios criados com IA antes de gastar mais ou publicar. Usar quando alguém disser "/auditor-video-ia", "revisa esse prompt", "audi… |
| Entradas (gatilhos) | /auditor-video-ia, revisa esse prompt, audita esse vídeo, regenero?, dá pra consertar?, controle de qualidade, preflight, postflight, deriva de identidade, falha de mãos/lip-sync, confere o CTA/produto/claims |
| Ferramentas citadas | python, seedance |
| Processo (cabeçalhos) | /auditor-video-ia — Preflight, postflight e decisão → Entradas → Preflight → Postflight → Passo 1 — Reconstruir o contrato → Passo 2 — Preflight → Passo 3 — Postflight técnico → Arquivo → Imagem → Áudio |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references, scripts · SKILL.md com 6,063 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/checa-prompt.py`

## Cluster

[video-ia](../clusters/video-ia.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
