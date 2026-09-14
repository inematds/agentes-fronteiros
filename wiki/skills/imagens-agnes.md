---
type: Skill
title: imagens-agnes
description: Gera IMAGENS avulsas com a API Agnes AI (agnes-image-2.1-flash) a custo US$ 0, com todos os parâmetros e armadilhas já MEDIDOS. Use SEMPRE que o usuário pedir "gera uma imagem", "cria uma arte/ilustração",
  "imagem de X"…
resource: file:///home/nmaldaner/.claude/skills/imagens-agnes/SKILL.md
tags:
- skill
- imagens
sources:
- path: /home/nmaldaner/.claude/skills/imagens-agnes/SKILL.md
  author: human:nei
  last_modified: '2026-07-17'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/imagens
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - python
  gatilhos:
  - gera uma imagem
  - cria uma arte/ilustração
  - imagem de X
  - thumbnail
  - capa
  - mockup
  tamanho_skill_md: 3117
migracao:
  estagio: inventariado
  cluster: imagens
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# imagens-agnes

## Descrição (do SKILL.md)

Gera IMAGENS avulsas com a API Agnes AI (agnes-image-2.1-flash) a custo US$ 0, com todos os parâmetros e armadilhas já MEDIDOS. Use SEMPRE que o usuário pedir "gera uma imagem", "cria uma arte/ilustração", "imagem de X", "thumbnail", "capa", "mockup", ou quiser text2img/img2img/edição via Agnes. Cobre proporções, resoluções 1K-4K, referência de imagem (img2img), e as regras que evitam os defeitos conhecidos (texto, cauda/cabeça dupla, contaminação de estilo, filtro de conteúdo em PT). NÃO use para transformar história em filme (aí é videos-agnes).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Gera IMAGENS avulsas com a API Agnes AI (agnes-image-2.1-flash) a custo US$ 0, com todos os parâmetros e armadilhas já MEDIDOS. Use SEMPRE que o usuário pedir… |
| Entradas (gatilhos) | gera uma imagem, cria uma arte/ilustração, imagem de X, thumbnail, capa, mockup |
| Ferramentas citadas | python |
| Processo (cabeçalhos) | imagens-agnes — geração de imagem (Agnes AI, US$ 0) → Fatos MEDIDOS (fonte: `~/projetos/agnes-nei/NOTAS-API.md`, ~70 chamadas reais) → Defeitos conhecidos e como evitar → Estilos testados (matriz 10×2) → Resoluções |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 3,117 chars |

## Cluster

[imagens](../clusters/imagens.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
