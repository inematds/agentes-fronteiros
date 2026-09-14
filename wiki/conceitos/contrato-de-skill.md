---
type: Conceito
title: Contrato de skill
description: Toda skill migrada tem um contrato YAML com trigger, input, output, tools e acceptance — a skill vira uma função operacional da empresa.
tags: [contrato, skill, acceptance]
sources:
  - { path: ../raw/2026-09-14-plano-migracao-agentes-skills.md, author: "human:nei", last_modified: "2026-09-14" }
generated: { by: "claude-fable-5-1/2026-09-14", at: "2026-09-14T17:30:00Z" }
status: stable
related: [conceitos/plano-migracao, conceitos/loop-de-validacao]
---

# Contrato de skill (etapa 8)

Template: `migracao/template-contrato.yaml`. Contratos-piloto: `migracao/contratos/{reels,video-explicativo,curso}.yaml`.

```yaml
skill: reels
trigger: [criar reel, vídeo curto, short, vídeo vertical]
input:
  tema: obrigatório
  publico: opcional
  duracao: 30-60s
  fonte: texto/url/video
output: { formato: mp4, aspect_ratio: "9:16", duracao_max: 60s }
tools: [web, image_gen, ffmpeg, tts]
acceptance:
  - gancho <= 3 segundos
  - sem texto cortado
  - áudio sincronizado
  - fontes verificadas
  - duração <= 60s
```

## Regras
- `acceptance` é verificável: cada item vira um check no loop (idealmente automatizado em `agent/tools/validate_*.py`).
- `trigger` alimenta a `description` do SKILL.md (roteamento).
- `tools` é lista fechada: a skill não pode inventar ferramenta fora dela sem atualizar o contrato.
- O contrato é copiado para `agent/skills/<nome>/contrato.yaml` quando a skill é migrada.
