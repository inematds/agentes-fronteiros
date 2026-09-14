---
type: Skill
title: videos-cursos-inema
description: 'Gera os vídeos de um curso INEMA a partir do site do curso, em 3 partes selecionáveis: landing, um vídeo por trilha, e/ou uma aula completa por módulo/dia. Aceita pedidos parciais.'
resource: file:///home/nmaldaner/.claude/skills/videos-cursos-inema/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/videos-cursos-inema/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/curso
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 13
  subpastas:
  - assets
  - references
  - scripts
  scripts:
  - assets/spec-template.mjs
  - scripts/build.mjs
  - scripts/engine.mjs
  - scripts/fetch-fonts.mjs
  - scripts/tts-inemavox.mjs
  - scripts/voice-sample.mjs
  - scripts/write-txt.mjs
  ferramentas:
  - chatterbox
  - ffmpeg
  - flux
  - github
  - hyperframes
  - inemavox
  - node
  - tts
  gatilhos: []
  tamanho_skill_md: 11399
migracao:
  estagio: inventariado
  cluster: curso
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# videos-cursos-inema

## Descrição (do SKILL.md)

Gera os vídeos de um curso INEMA a partir do site do curso, em 3 partes selecionáveis: landing, um vídeo por trilha, e/ou uma aula completa por módulo/dia. Aceita pedidos parciais.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Gera os vídeos de um curso INEMA a partir do site do curso, em 3 partes selecionáveis: landing, um vídeo por trilha, e/ou uma aula completa por módulo/dia. Ace… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | chatterbox, ffmpeg, flux, github, hyperframes, inemavox, node, tts |
| Processo (cabeçalhos) | Vídeos de Cursos INEMA → As 3 partes (o usuário escolhe quais fazer) → Configuração (voz, provedor, formato) — com defaults → Fluxo de trabalho → 1. Setup do projeto → copie os scripts da skill pra raiz do projeto (ao lado de specs.mjs): → fontes locais (Sora/Inter/JetBrains) — NÃO usar CDN: → 2. Detectar formato e extrair o conteúdo do site → 3. Escrever os specs → 4. Gerar (pipeline por id) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references, scripts · SKILL.md com 11,399 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/spec-template.mjs`
- `scripts/build.mjs`
- `scripts/engine.mjs`
- `scripts/fetch-fonts.mjs`
- `scripts/tts-inemavox.mjs`
- `scripts/voice-sample.mjs`
- `scripts/write-txt.mjs`

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
