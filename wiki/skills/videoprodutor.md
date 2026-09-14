---
type: Skill
title: videoprodutor
description: O Produtor — orquestra link/assunto → vídeo profissional ponta a ponta (plano, direção, imagem/SVG, voz, render em 3 camadas), 16:9 e 9:16, dark premium INEMA.CLUB, tudo local. Use quando o
  usuário der um link/assunto/f…
resource: file:///home/nmaldaner/.claude/skills/videoprodutor/SKILL.md
tags:
- skill
- video-explicativo
sources:
- path: /home/nmaldaner/.claude/skills/videoprodutor/SKILL.md
  author: human:nei
  last_modified: '2026-06-25'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/video-explicativo
skill:
  versao: 0.2.0
  invocacao_pelo_modelo: true
  arquivos: 21
  subpastas:
  - references
  - scripts
  scripts:
  - scripts/composition-template.mjs
  - scripts/fetch-fonts.mjs
  - scripts/gen-imgs.mjs
  - scripts/svg-icons.mjs
  ferramentas:
  - ffmpeg
  - flux
  - hyperframes
  - node
  - python
  - tts
  gatilhos:
  - produz o vídeo
  - do link ao vídeo
  - vídeo profissional disso
  - monta o vídeo inteiro
  - fábrica de vídeo
  tamanho_skill_md: 5647
migracao:
  estagio: inventariado
  cluster: video-explicativo
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# videoprodutor

## Descrição (do SKILL.md)

O Produtor — orquestra link/assunto → vídeo profissional ponta a ponta (plano, direção, imagem/SVG, voz, render em 3 camadas), 16:9 e 9:16, dark premium INEMA.CLUB, tudo local. Use quando o usuário der um link/assunto/fonte e quiser o VÍDEO PROFISSIONAL completo (propaganda ou explicativo) saindo de uma vez — não só roteiro, não só imagem, não só prompt. Acione para "produz o vídeo", "do link ao vídeo", "vídeo profissional disso", "monta o vídeo inteiro", "fábrica de vídeo".

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | O Produtor — orquestra link/assunto → vídeo profissional ponta a ponta (plano, direção, imagem/SVG, voz, render em 3 camadas), 16:9 e 9:16, dark premium INEMA.… |
| Entradas (gatilhos) | produz o vídeo, do link ao vídeo, vídeo profissional disso, monta o vídeo inteiro, fábrica de vídeo |
| Ferramentas citadas | ffmpeg, flux, hyperframes, node, python, tts |
| Processo (cabeçalhos) | videoprodutor (o Produtor) → As 3 camadas (o que faz um vídeo "profissional", não slideshow) → Linha de montagem (sempre nesta ordem) → Pré-flight (checar dependências) → Regras de ouro (não-negociáveis) → Como usar (resumo) → Scripts (molde testado — caso Hormozi) → Referências |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: references, scripts · SKILL.md com 5,647 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/composition-template.mjs`
- `scripts/fetch-fonts.mjs`
- `scripts/gen-imgs.mjs`
- `scripts/svg-icons.mjs`

## Cluster

[video-explicativo](../clusters/video-explicativo.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
