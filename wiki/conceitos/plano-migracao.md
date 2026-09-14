---
type: Playbook
title: Plano de migração (agentes → generalista + skills)
description: As 10 etapas do plano de migração e a estratégia prática de começar por reels, vídeo explicativo e curso.
tags: [migracao, plano, skills, agente-base]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/agente-base, conceitos/contrato-de-skill, conceitos/loop-de-validacao, conceitos/aprendizado-permanente, conceitos/router]
---

# Plano de migração

Fonte: [plano original](../raw/2026-09-14-plano-migracao-agentes-skills.md). Versão operacional em `PLANO.md` na raiz do repo.

## Tese
Trocar **agentes especializados e isolados** por **agente generalista → skills → ferramentas reutilizáveis → loops de verificação → aprendizado contínuo**. "Não precisamos criar mais agentes. Precisamos ensinar agentes gerais a trabalhar do nosso jeito."

## Etapas
1. **Inventariar** — agente → tarefa → entradas → ferramentas → processo → saída → validação; achar repetição. → `wiki/skills/`, `wiki/clusters/`
2. **Agente base** — um agente geral que usa arquivos, terminal, web, MCP, APIs, memória, skills. → [agente-base](agente-base.md)
3. **Agentes viram skills** — SKILL.md com objetivo, quando usar, entradas, saídas, processo, ferramentas, regras, qualidade, validação.
4. **Código repetido vira tool** — `tools/render_video.py`, `transcribe.py`, … a skill manda executar, não reescreve.
5. **Progressive disclosure** — SKILL.md enxuto + `references/`, `scripts/`, `templates/`.
6. **Correção vira aprendizado** — corrigir o sistema, não a saída. → [aprendizado-permanente](aprendizado-permanente.md)
7. **Loop dentro da skill** — planejar → executar → inspecionar → criticar → corrigir → testar. → [loop-de-validacao](loop-de-validacao.md)
8. **Contrato** — trigger/input/output/tools/acceptance. → [contrato-de-skill](contrato-de-skill.md)
9. **Router** — o agente identifica a intenção. → [router](router.md)
10. **Sistema vivo** — INTENÇÃO → CONTEXTO → SKILL → FERRAMENTAS → LOOP → APRENDIZADO.

## Estratégia prática
Começar por 3: `reels`, `video-explicativo`, `curso`. Nove passos por piloto (= os estágios `migracao.estagio` das páginas de skill). Depois, aplicar o padrão aprovado aos demais.

## Lacuna registrada
O plano cita `cria-books`; não existe skill local com esse nome (2026-09-14).
