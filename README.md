# agentes-fronteiros

[![agentes-fronteiros](guia/assets/banner.jpg)](https://inematds.github.io/agentes-fronteiros/guia/)

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/agentes-fronteiros/guia/**

Projeto de **migração** do ecossistema INEMA de agentes especializados para
**um agente generalista + skills com contrato + ferramentas reutilizáveis +
loop de validação + base de conhecimento viva**.

Três referências combinadas:

| Referência | O que entra aqui |
|---|---|
| **Plano de migração** (`PLANO.md`) | As 10 etapas: inventário → agente base → skills → tools → progressive disclosure → aprendizado → loop → contrato → router → sistema vivo. |
| **eve (Vercel)** — modelo de pastas | O agente é um diretório: `agent/instructions.md`, `skills/`, `tools/`, `connections/`, `channels/`, `schedules/`, `subagents/`, `hooks/`, `lib/`, `sandbox/` e `evals/` ao lado. Aqui é **convenção de pastas**, não o runtime TypeScript. |
| **OKF + LLM wiki (Karpathy)** | A base de conhecimento em `wiki/` é um bundle OKF: markdown + YAML frontmatter (`type` obrigatório, `sources`, `generated`, `verified`, `status`, `stale_after`), `index.md` e `log.md` reservados. O agente mantém a wiki: ingere fontes brutas de `wiki/raw/`, consolida em conceitos, atualiza índice e log. |

## Estrutura

```text
agentes-fronteiros/
├── README.md · PLANO.md · ARQUITETURA.md · CLAUDE.md · FALHAS.md
├── agent/                 # layout eve (convenção)
│   ├── agent.yaml         # modelo, esforço, política de roteamento
│   ├── instructions.md    # prompt sempre-ligado do agente generalista (INEMA AGENT)
│   ├── skills/            # skills migradas (SKILL.md + references/ + scripts/ + contrato.yaml)
│   ├── tools/             # ferramentas reutilizáveis (ffmpeg, transcrição, render, validação)
│   ├── connections/ channels/ schedules/ subagents/ hooks/ lib/ sandbox/
├── evals/                 # tarefas reais usadas para aprovar cada skill migrada
├── wiki/                  # bundle OKF (base de conhecimento)
│   ├── SCHEMA.md          # convenções da wiki (o "schema" do LLM wiki)
│   ├── index.md · log.md  # reservados (listagem + histórico)
│   ├── raw/               # fontes brutas ingeridas (nunca editadas)
│   ├── conceitos/         # conceitos curados (okf, eve, llm-wiki, contrato-de-skill, loop...)
│   ├── skills/            # 1 conceito por skill existente (gerado por tools/inventario.py)
│   ├── agentes/           # 1 conceito por agente existente
│   └── clusters/          # sobreposições detectadas (várias skills, mesma intenção)
├── migracao/
│   ├── template-contrato.yaml · template-SKILL.md
│   └── contratos/         # reels.yaml · video-explicativo.yaml · curso.yaml (pilotos)
├── tools/
│   ├── inventario.py      # varre ~/.claude/skills e ~/.claude/agents → wiki/skills, wiki/agentes, wiki/clusters, index
│   └── wiki_lint.py       # valida frontmatter OKF (falha se faltar `type`), links e reservados
└── interface/
    ├── server.py          # servidor local (stdlib) — API sobre a wiki
    └── index.html         # interface de migração (kanban por estágio, clusters, contratos, wiki)
```

## Uso rápido

```bash
cd ~/projetos/agentes-fronteiros

# 1. (re)gerar o inventário a partir das skills/agentes instalados
python3 tools/inventario.py

# 2. validar a wiki
python3 tools/wiki_lint.py

# 3. abrir a interface de migração
python3 interface/server.py          # http://127.0.0.1:8765
```

## Estado de migração mora na wiki

Cada skill tem **uma página** em `wiki/skills/<nome>.md`. O estágio de migração
fica no frontmatter dessa página (campo `migracao:`), que a interface lê e
escreve. Não existe um `state.json` paralelo: a wiki é a única fonte de verdade.

Estágios (os 9 passos da estratégia prática do plano, compactados):

`inventariado → mapeado → skill → tools → contrato → loop → testado → aprovado` (ou `descontinuado`)

## Pilotos

O plano manda começar por 3 agentes. Os contratos-piloto estão em `migracao/contratos/`:

- **reels** → cluster `reels` (`reel-edita-inema`, `reel-edita-inematds`, `forja-reel`, `roteirista-inema`)
- **video-explicativo** → cluster `video-explicativo` (`video-explicativo`, `videoprodutor`, `faceless-explainer`)
- **curso** → cluster `curso` (`formato-curso-v5`, `formato-curso-v2`, `revisar-curso`, `videos-cursos-inema`)

`cria-books`, citado no plano, não existe como skill local: fica registrado como lacuna.
