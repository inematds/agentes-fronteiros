---
type: Reference
title: Schema da wiki (convenções OKF + LLM wiki)
description: Como esta wiki é organizada, quais campos de frontmatter existem e como o agente deve ingerir, consolidar, indexar e registrar.
tags: [wiki, okf, schema, convencoes]
generated: { by: "human:nei", at: "2026-09-14T00:00:00Z" }
status: stable
---

# Schema da wiki

Esta pasta é um **bundle OKF** (Open Knowledge Format v0.2) mantido no estilo
**LLM wiki**: o agente lê fontes brutas e mantém as páginas; o humano revisa.

## Pastas

| Pasta | Conteúdo | Quem escreve |
|---|---|---|
| `raw/` | fontes brutas, nome `AAAA-MM-DD-<slug>.md`. **Nunca editar.** | humano (cola) ou agente (ingestão) |
| `conceitos/` | conceitos curados do domínio (okf, eve, contrato de skill, loop…) | agente, revisado por humano |
| `skills/` | 1 página por skill instalada em `~/.claude/skills` | `tools/inventario.py` (+ campo `migracao` pela interface) |
| `agentes/` | 1 página por agente em `~/.claude/agents` | `tools/inventario.py` |
| `clusters/` | grupos de skills que disputam a mesma intenção | `tools/inventario.py` |

Arquivos reservados em qualquer nível: `index.md` (listagem) e `log.md` (histórico).
Todo outro `.md` é um **conceito**; o ID é o caminho sem `.md` (ex.: `skills/video-explicativo`).

## Frontmatter

```yaml
---
type: Skill                      # OBRIGATÓRIO. Tipos usados: Skill, Agente, Cluster, Conceito, Reference, Playbook, Contrato
title: Vídeo Explicativo
description: uma linha
resource: file:///home/.../SKILL.md   # opcional, URI canônica do ativo
tags: [video, hyperframes]
sources:                          # proveniência
  - path: raw/2026-09-14-plano-migracao-agentes-skills.md
    author: human:nei
    last_modified: 2026-09-14
generated: { by: "inventario.py/1.0", at: "2026-09-14T17:30:00Z" }
verified:                         # lista de eventos de verificação
  - { by: "human:nei", at: "2026-09-15T10:00:00Z" }
status: draft                     # draft | stable | deprecated
stale_after: 2026-12-31           # depois disso, reconsolidar
related: [skills/videoprodutor, clusters/video-explicativo]   # arestas do grafo (IDs de conceito)
migracao:                         # campo próprio deste projeto (OKF tolera campos desconhecidos)
  estagio: inventariado
  cluster: video-explicativo
  destino: ""
  notas: ""
  atualizado: 2026-09-14
---
```

Atores: `human:<id>` · `<produtor>/<versão>` (agente/script) · `process:<id>`.

Trust tier derivada de `verified`: sem `verified` = não verificado · `by` de processo/agente = confirmado por máquina · `by` humano = revisado por humano.

## Operações do agente (LLM wiki)

1. **Ingerir**: salvar fonte em `raw/` com data. Não resumir dentro do raw.
2. **Consolidar**: para cada entidade citada, criar/atualizar conceito. Fatos vêm com link pra fonte. Fato que mudou vira "Superado" (não apagar). Preencher `sources`, `generated`.
3. **Ligar**: preencher `related` com IDs de conceito; links no corpo como `[texto](../pasta/conceito.md)`.
4. **Indexar**: regerar `index.md` da pasta (uma linha por conceito: `- [title](arquivo.md) — description`).
5. **Registrar**: linha em `log.md` no topo: `| data | ator | ação | conceitos |`.
6. **Lint**: `python3 tools/wiki_lint.py` — falha se faltar `type`, link relativo quebrado, ou `index.md`/`log.md` com frontmatter de conceito.

## Consulta (progressive disclosure)

Ordem de leitura barata → cara: `wiki/index.md` → `index.md` da pasta → frontmatter do conceito → corpo do conceito → `raw/`.
