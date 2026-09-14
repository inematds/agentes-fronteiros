---
type: Conceito
title: OKF — Open Knowledge Format
description: Formato aberto, vendor-neutral, para conhecimento como markdown + YAML frontmatter em bundles versionáveis; usado como formato desta wiki.
tags: [okf, wiki, formato, conhecimento]
resource: file:///home/nmaldaner/projetos/okf/okf/SPEC.md
sources:
  - { path: /home/nmaldaner/projetos/okf/okf/SPEC.md, author: "human:nei", last_modified: "2026-09-14" }
  - { path: /home/nmaldaner/projetos/cerebro-vip/content/projetos/okf.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/llm-wiki-karpathy]
---

# OKF — Open Knowledge Format (v0.2)

**Um formato, não uma plataforma.** Um bundle é uma árvore de arquivos `.md` com YAML frontmatter, sem SDK nem API proprietária. Repositório local: `~/projetos/okf` (guia em `guia/`, spec em `okf/SPEC.md`).

## Regras que esta wiki adota
- **Bundle** = diretório; estrutura de pastas é livre, a semântica vem do frontmatter e dos links.
- **Conceito** = qualquer `.md` que não seja `index.md` (listagem) ou `log.md` (histórico). *Concept ID* = caminho sem `.md`.
- **`type` é o único campo obrigatório.** Tipos não são registrados centralmente; consumidores toleram tipos e campos desconhecidos.
- Famílias de campos:
  - identidade: `title`, `description`, `resource`, `tags`
  - proveniência: `sources` (`author`, `usage_count`, `last_modified`, `usage_window`) — OKF registra **sinais** de credibilidade, não um veredito
  - confiança: `generated {by, at}` e `verified [{by, at}]` → *trust tier*: não verificado / confirmado por máquina / revisado por humano
  - ciclo de vida: `status: draft|stable|deprecated`, `stale_after`
- Atores: `human:<id>`, `<produtor>/<versão>`, `process:<id>`.
- **Divulgação progressiva**: `index.md` por pasta permite ler barato antes de abrir conceitos.
- **Grafo, não só árvore**: links markdown entre conceitos são arestas de primeira classe.
- v0.2 adiciona *Attested Computation* (conceito com computação + executor + attester); não usado aqui por enquanto.

## Por que aqui
Serve de esquema para a memória operacional do agente generalista: cada skill, agente, cluster e decisão é um conceito com proveniência e status, e a interface de migração lê/escreve o frontmatter sem banco paralelo.
