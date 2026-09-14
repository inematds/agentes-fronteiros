---
type: Conceito
title: LLM wiki (estilo Karpathy)
description: Base de conhecimento mantida pelo próprio agente — fontes brutas entram, o modelo consolida em páginas curadas, indexa, registra e lint-a; o humano revisa.
tags: [wiki, karpathy, memoria, conhecimento]
sources:
  - { path: /home/nmaldaner/projetos/cerebro-vip/CAMADA-WIKI.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/okf, conceitos/aprendizado-permanente]
---

# LLM wiki (estilo Karpathy)

Ideia: em vez de RAG sobre documentos soltos, o LLM mantém **uma wiki persistente** em markdown. Cada fonte nova é ingerida e **incorporada** nas páginas existentes (não só anexada), com índice, log de mudanças e um arquivo de esquema que descreve as convenções. O conhecimento fica compilado, navegável e versionado em git.

## Componentes (como aplicados aqui)
| Componente | Aqui |
|---|---|
| fontes brutas imutáveis | `wiki/raw/AAAA-MM-DD-<slug>.md` |
| páginas curadas | `wiki/conceitos/`, `wiki/skills/`, `wiki/agentes/`, `wiki/clusters/` |
| índice barato para o prompt | `index.md` por pasta + `wiki/index.md` |
| log de mudanças | `wiki/log.md` (tabela, mais recente no topo) |
| esquema / convenções | `wiki/SCHEMA.md` |
| operações: ingerir · consolidar · indexar · registrar · consultar · lint | `tools/inventario.py`, `tools/wiki_lint.py`, e o próprio agente |

## Regras práticas
- Nunca apagar fato antigo: marcar **superado** (`status: deprecated` ou seção "Superado") e manter o link pra fonte.
- `sources` são backlinks imutáveis (só acrescenta). `related` são arestas do grafo.
- Consulta em ordem barato → caro: índice raiz → índice da pasta → frontmatter → corpo → raw.
- O mesmo desenho já existe no `cerebro-vip` (`wiki/<slug>.md` com `fontes`/`relacionados`); aqui os campos seguem os nomes do [OKF](okf.md).
