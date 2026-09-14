---
type: Cluster
title: Publicação / portal / landing
description: 6 skills disputam a intenção “Publicação / portal / landing”.
tags:
- cluster
- publicacao
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/anuncio-edita
- skills/atualiza-portal
- skills/audit-ablacao
- skills/projetos-landing-guia
- skills/property-360
- skills/web-artifacts-builder
cluster:
  id: publicacao
  membros:
  - anuncio-edita
  - atualiza-portal
  - audit-ablacao
  - projetos-landing-guia
  - property-360
  - web-artifacts-builder
---

# Cluster: Publicação / portal / landing

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [anuncio-edita](../skills/anuncio-edita.md) |  | 9 | chatterbox, ffmpeg, inemavox, python, whisper |
| [atualiza-portal](../skills/atualiza-portal.md) | Publica curso ou projeto (URL github.io) nas 3 superfícies INEMA — portal (inema.club), inemabuscas e catálog… | 1 | flux, github, node, supabase, telegram |
| [audit-ablacao](../skills/audit-ablacao.md) | Auditoria de ablação (somente diagnóstico) do CLAUDE.md, das skills e dos hooks de um projeto ou da config gl… | 0 |  |
| [projetos-landing-guia](../skills/projetos-landing-guia.md) | Pagina unica de LANDING + GUIA DE USO de um projeto, self-contained em guia/index.html, padrao INEMA dark amb… | 1 | ffmpeg, flux, github, node, openai |
| [property-360](../skills/property-360.md) | Transforma várias fotos comuns de um MESMO cômodo (ou só uma descrição em texto) numa panorâmica 360° equiret… | 0 | flux, gemini, magnific, python |
| [web-artifacts-builder](../skills/web-artifacts-builder.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web tec… | 2 | node, playwright |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`flux` (3×), `node` (3×), `ffmpeg` (2×), `python` (2×), `github` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
