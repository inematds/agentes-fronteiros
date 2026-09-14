---
type: Cluster
title: ComfyUI
description: 6 skills disputam a intenção “ComfyUI”.
tags:
- cluster
- comfy
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- skills/comfy
- skills/comfy-build
- skills/comfy-debug
- skills/comfy-deploy
- skills/comfy-director
- skills/comfy-relay
cluster:
  id: comfy
  membros:
  - comfy
  - comfy-build
  - comfy-debug
  - comfy-deploy
  - comfy-director
  - comfy-relay
---

# Cluster: ComfyUI

Skills que respondem à mesma intenção. Quanto maior o cluster, maior o ganho de consolidar em **uma** skill com `references/` por variante.

| Skill | Descrição | Scripts | Ferramentas |
|---|---|---|---|
| [comfy](../skills/comfy.md) | Generate images, videos, audio, and 3D via ComfyUI — CLI surface, workflow creation hierarchy (template → fra… | 0 | comfyui, ffmpeg, flux, gemini, github |
| [comfy-build](../skills/comfy-build.md) | Build a custom ComfyUI environment on the Comfy developer platform with comfy-cli: turn a local install, a Co… | 0 | comfyui, github, node, python |
| [comfy-debug](../skills/comfy-debug.md) | Debugging skill for the comfy CLI — failed workflows, stuck jobs, error envelopes, and the fastest path from… | 0 | comfyui, node, python |
| [comfy-deploy](../skills/comfy-deploy.md) | Run a Comfy Build release as a serverless deployment with comfy-cli. Use whenever the user wants to deploy, s… | 0 | comfyui, github, node |
| [comfy-director](../skills/comfy-director.md) | Use when asked to make a narrative video — an ad, brand film, short, trailer, music video, or any multi-shot… | 0 | ffmpeg, kling, tts |
| [comfy-relay](../skills/comfy-relay.md) | How to present and interact during comfy creative work (images, video, audio) — show visual previews in chat,… | 0 | ffmpeg, node |

## Repetição detectada (etapa 4 — candidatas a `agent/tools/`)

`node` (5×), `comfyui` (4×), `ffmpeg` (3×), `github` (3×), `python` (3×), `kling` (2×), `tts` (2×)

## Decisão de consolidação

_preencher: skill-mãe, o que vira reference, o que vira tool, o que é descontinuado_
