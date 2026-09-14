---
type: Cluster
title: Printing Press (CLI a partir de API)
description: 9 skills disputam a intenção “Printing Press (CLI a partir de API)”.
tags:
- cluster
- printing-press
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/printing-press
- skills/printing-press-catalog
- skills/printing-press-import
- skills/printing-press-output-review
- skills/printing-press-polish
- skills/printing-press-publish
- skills/printing-press-reprint
- skills/printing-press-retro
- skills/printing-press-score
cluster:
  id: printing-press
  membros:
  - printing-press
  - printing-press-catalog
  - printing-press-import
  - printing-press-output-review
  - printing-press-polish
  - printing-press-publish
  - printing-press-reprint
  - printing-press-retro
  - printing-press-score
---

# Cluster: Printing Press (CLI a partir de API)

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [printing-press](../skills/printing-press.md) | Generate a ship-ready CLI for an API with a lean research -> generate -> build -> shipcheck loop. | 0 | agent-browser, github, mcp, playwright, python |
| [printing-press-catalog](../skills/printing-press-catalog.md) | Browse and install pre-built Go CLIs for popular APIs from the catalog | 0 | github |
| [printing-press-import](../skills/printing-press-import.md) | Bring a published CLI from the public library into the internal library so it's identical to a freshly-genera… | 4 | github |
| [printing-press-output-review](../skills/printing-press-output-review.md) | Internal sub-skill: agentic review of a printed CLI's sampled command output for plausibility issues that rul… | 0 |  |
| [printing-press-polish](../skills/printing-press-polish.md) | Polish a generated CLI to pass verification and become publish-ready. Runs diagnostics (dogfood, verify, scor… | 0 | github, mcp |
| [printing-press-publish](../skills/printing-press-publish.md) | Publish a generated CLI to the printing-press-library repo | 0 | github, mcp |
| [printing-press-reprint](../skills/printing-press-reprint.md) | Regenerate an existing printed CLI from scratch under the current Printing Press, with prior research and pri… | 0 | mcp, python |
| [printing-press-retro](../skills/printing-press-retro.md) | Run a retrospective after generating a CLI. Identifies systemic improvements to the Printing Press — template… | 0 | github |
| [printing-press-score](../skills/printing-press-score.md) | Score a generated CLI against the Steinberger bar, compare two CLIs side-by-side | 0 | github |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`github` (7×), `mcp` (4×), `python` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
