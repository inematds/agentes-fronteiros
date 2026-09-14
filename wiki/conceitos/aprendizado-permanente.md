---
type: Conceito
title: Aprendizado permanente (correção vira sistema)
description: Nunca corrigir só a saída — investigar por que errou e corrigir a skill, a regra, o exemplo ou o script que produziu a saída.
tags: [aprendizado, falhas, correcao]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/loop-de-validacao, conceitos/llm-wiki-karpathy]
---

# Aprendizado permanente (etapa 6)

```text
executa → erro identificado → agente corrige → investiga POR QUE errou
→ decide onde corrigir (skill | regra | exemplo | script) → executa de novo → valida
```

> Nunca corrigir apenas a saída. Corrigir o sistema que produziu a saída.

## Onde cada correção vai
| Causa | Correção vai para |
|---|---|
| a skill não explicou o caso | `SKILL.md` ou `references/` da skill |
| regra de negócio faltando | `agent/instructions.md` ou `CLAUDE.md` |
| exemplo ruim / ausente | `references/exemplos.md` |
| código refeito errado | `agent/tools/*.py` (proteção: teto, retry, guard, validação) |
| conhecimento desatualizado | `wiki/` (conceito + `log.md`) |

## Registro
- `FALHAS.md` na raiz: `| data | o que quebrou | menor correção | prompt \| infra |` — uma linha, mais recente no topo.
- `wiki/log.md`: linha com o conceito/skill alterado.
