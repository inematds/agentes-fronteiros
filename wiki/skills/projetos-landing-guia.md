---
type: Skill
title: projetos-landing-guia
description: 'Pagina unica de LANDING + GUIA DE USO de um projeto, self-contained em guia/index.html, padrao INEMA dark ambar, pronta pra GitHub Pages. Gatilho: "pagina/landing/site/guia de uso do projeto",
  ou GitHub Pages para um re…'
resource: file:///home/nmaldaner/.claude/skills/projetos-landing-guia/SKILL.md
tags:
- skill
- publicacao
sources:
- path: /home/nmaldaner/.claude/skills/projetos-landing-guia/SKILL.md
  author: human:nei
  last_modified: '2026-09-14'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/publicacao
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 3
  subpastas:
  - assets
  scripts:
  - assets/gerar-banner.sh
  ferramentas:
  - ffmpeg
  - flux
  - github
  - node
  - openai
  gatilhos:
  - pagina/landing/site/guia de uso do projeto
  tamanho_skill_md: 14987
migracao:
  estagio: inventariado
  cluster: publicacao
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# projetos-landing-guia

## Descrição (do SKILL.md)

Pagina unica de LANDING + GUIA DE USO de um projeto, self-contained em guia/index.html, padrao INEMA dark ambar, pronta pra GitHub Pages. Gatilho: "pagina/landing/site/guia de uso do projeto", ou GitHub Pages para um repo.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Pagina unica de LANDING + GUIA DE USO de um projeto, self-contained em guia/index.html, padrao INEMA dark ambar, pronta pra GitHub Pages. Gatilho: "pagina/land… |
| Entradas (gatilhos) | pagina/landing/site/guia de uso do projeto |
| Ferramentas citadas | ffmpeg, flux, github, node, openai |
| Processo (cabeçalhos) | projetos-landing-guia → Regra de repositorio (nao quebrar) → Fluxo → Referencia no README (obrigatorio) → Invariantes de design (nao quebrar) → Estrutura (secoes do template) → Publicar no GitHub Pages (via GitHub Actions) → 1. garanta que nao ha segredos versionados → 2. NAO deixe placeholder do template sem preencher → 3. workflow de deploy estatico (path:'.', serve da raiz — guia fica em .../<repo>/guia/) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets · SKILL.md com 14,987 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/gerar-banner.sh`

## Cluster

[publicacao](../clusters/publicacao.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
