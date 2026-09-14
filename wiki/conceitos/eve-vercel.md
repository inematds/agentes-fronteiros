---
type: Conceito
title: eve (Vercel) — modelo de pastas
description: Framework filesystem-first da Vercel para agentes duráveis; o agente é um diretório com slots nomeados. Adotado aqui como convenção de pastas para o agente generalista.
tags: [eve, vercel, layout, pastas, agentes]
resource: file:///home/nmaldaner/projetos/eve/docs/reference/project-layout.md
sources:
  - { path: /home/nmaldaner/projetos/eve/README.md, author: "vercel", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/projetos/eve/docs/reference/project-layout.md, author: "vercel", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/projetos/eve/docs/subagents.mdx, author: "vercel", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/projetos/eve/docs/skills.mdx, author: "vercel", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/agente-base, conceitos/router]
---

# eve (Vercel) — "the filesystem is the authoring interface"

Repositório local: `~/projetos/eve` (guia em https://inematds.github.io/eve/guia/).

## Layout recomendado
```text
my-agent/
├── package.json · tsconfig.json
├── agent/
│   ├── agent.ts            # modelo e config de runtime
│   ├── instructions.md     # system prompt sempre ligado (obrigatório)
│   ├── instrumentation.ts
│   ├── channels/           # por onde chega mensagem (Slack, Discord, HTTP…)
│   ├── connections/        # MCP e serviços externos
│   ├── hooks/              # ciclo de vida
│   ├── skills/             # procedimentos carregados sob demanda (load_skill)
│   ├── lib/                # helpers compartilhados
│   ├── sandbox/            # workspace semeado
│   ├── tools/              # funções tipadas (defineTool + zod)
│   ├── schedules/          # cron (markdown fire-and-forget ou handler)
│   └── subagents/<id>/     # agente filho: agent.ts (com description) + slots próprios
└── evals/                  # irmão de agent/, não dentro
```

## Regras que importam para a migração
- **Skill = instruções, não superfície de execução.** A descrição é *dica de roteamento*: escrever como a tarefa que dispara ("Use when the user needs a release checklist"). Comportamento tipado vai para `tools/`.
- **Subagente declarado não herda nada da raiz** (instruções, tools, skills, sandbox, hooks). Se dois precisam do mesmo procedimento: duplicar o markdown ou compartilhar por `lib/`. `channels/` e `schedules/` são só da raiz.
- **`load_skill`** lê `SKILL.md`; referências irmãs (`references/checklist.md`) são relativas à pasta da skill — igual ao progressive disclosure da etapa 5 do plano.
- **Durável por padrão**: cada turno é um run durável; estado por `defineState`, nunca compartilhado entre pai e filho.

## Mapeamento para o Claude Code
Ver tabela em `ARQUITETURA.md` §1. Resumo: `instructions.md` → prompt do agente base; `skills/` → Skill tool; `subagents/<id>/agent.ts description` → frontmatter dos `.md` em `~/.claude/agents`; `tools/` → scripts Python com contrato CLI+JSON; `evals/` → tarefas reais em `evals/tarefas/`.
