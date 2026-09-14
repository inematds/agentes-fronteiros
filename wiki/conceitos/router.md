---
type: Conceito
title: Router de intenção
description: O usuário não diz qual skill usar — o agente identifica a intenção, escolhe o cluster e a skill, e usa maestro-roteador para modelo/esforço.
tags: [router, intencao, roteamento]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/.claude/skills/maestro-roteador/SKILL.md, author: "human:nei", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/.claude/agents/diretor-ecossistema.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: draft
related: [conceitos/agente-base, skills/maestro-roteador, agentes/diretor-ecossistema]
---

# Router (etapa 9)

```text
PEDIDO → ROUTER → qual intenção? → cluster → skill → contrato → loop
```

## Já existe (não criar um terceiro roteador)
- `maestro-roteador` (skill) — escolhe **modelo e esforço** para despachar trabalho.
- `diretor-ecossistema` (agente) — escolhe **qual ferramenta de vídeo** (pixflow / mdd / video-plan-editor / promptprof).

O router do agente base absorve os dois: primeiro **intenção → cluster** (tabela em `agent/instructions.md`), depois delega a escolha fina de ferramenta ao `diretor-ecossistema` quando o cluster é vídeo, e a escolha de modelo/esforço ao `maestro-roteador` quando vai despachar subagente.

## Regra para descrições de skill
A `description` do SKILL.md é a chave de roteamento. Formato: **o que faz + quando disparar (frases do usuário) + quando NÃO usar**. Skills que hoje competem pelo mesmo gatilho (ver `wiki/clusters/`) ou se fundem ou ganham `disable-model-invocation: true` (como já foi feito com `formato-curso-*`).
