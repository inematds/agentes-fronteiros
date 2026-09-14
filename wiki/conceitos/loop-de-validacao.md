---
type: Conceito
title: Loop de validação dentro da skill
description: A primeira versão é rascunho — planejar, executar, inspecionar, criticar, corrigir, testar; só entrega quando passa nos critérios de aceitação.
tags: [loop, validacao, qualidade]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/contrato-de-skill, conceitos/aprendizado-permanente]
---

# Loop de validação (etapa 7)

```text
INPUT → PLANEJAR → EXECUTAR → INSPECIONAR → CRITICAR → CORRIGIR → TESTAR → passou?
                                                                     não ↺ LOOP · sim → ENTREGA
```

## Como entra na skill migrada
Toda `SKILL.md` migrada tem uma seção `## Loop` com:
1. **Planejar** — listar cenas/etapas antes de gerar.
2. **Executar** — chamar `agent/tools/*` (nunca reescrever utilitário).
3. **Inspecionar** — abrir o resultado de verdade (frames, duração, lint HTML, contagem de palavras).
4. **Criticar** — comparar com `acceptance` do contrato, item a item.
5. **Corrigir** — mudar a causa, não o sintoma.
6. **Testar** — rodar o validador (`validate_*.py`) e só então entregar.

Teto de iterações: 3. Se não passar, entregar o melhor rascunho **dizendo o que falhou** e registrar em `FALHAS.md`.
