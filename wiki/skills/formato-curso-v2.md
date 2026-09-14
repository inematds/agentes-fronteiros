---
type: Skill
title: formato-curso-v2
description: Template e padroes de design para criar paginas HTML de cursos no formato INEMA.CLUB COM camada de aprendizagem por cima — progresso/marcar-lido, duvida, anotacoes/highlight no proprio texto,
  painel "minha jornada" (con…
resource: file:///home/nmaldaner/.claude/skills/formato-curso-v2/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/formato-curso-v2/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:32:36Z'
status: draft
related:
- clusters/curso
skill:
  versao: ''
  invocacao_pelo_modelo: false
  arquivos: 10
  subpastas:
  - assets
  - references
  scripts:
  - assets/learn.js
  ferramentas:
  - flux
  - hyperframes
  - node
  gatilhos:
  - minha jornada
  - formato de curso
  - template de curso
  tamanho_skill_md: 30149
migracao:
  estagio: mapeado
  cluster: curso
  destino: curso
  notas: piloto 3 (v2) — contrato em migracao/contratos/curso.yaml
  atualizado: '2026-09-14'
---

# formato-curso-v2

## Descrição (do SKILL.md)

Template e padroes de design para criar paginas HTML de cursos no formato INEMA.CLUB COM camada de aprendizagem por cima — progresso/marcar-lido, duvida, anotacoes/highlight no proprio texto, painel "minha jornada" (continuar de onde parei), export/import .json, sistema de temas trocavel (data-theme ortogonal ao .dark) + preferencias de leitura (tamanho/largura/entrelinha/fonte/acento). Tudo self-contained (HTML+Tailwind CDN+JS inline, sem build/backend, abre em file://), baseado no formato-curso v1 (dark premium ambar/ciano, SVG futurista, profundidade de modulos). Use esta skill SEMPRE que o usuario pedir para criar, editar ou revisar paginas HTML de curso — incluindo index de trilhas, paginas de modulos, componentes como navegacao, cards, topicos expansiveis, modais e slides — e tambem quando pedir os recursos de aprendizagem (progresso, marcar lido, duvida, anotacao, highlight, minha jornada, export/import, temas, modo leitura/sepia/foco/alto-contraste). Acione tambem quando o usuario mencionar trilhas, modulos, topicos, INEMA.CLUB, ou quando pedir para seguir o "formato de curso" ou "template de curso". Nao deixe de usar esta skill se o usuario mencionar qualquer coisa relacionada a paginas HTML de cursos ou ao projeto skillx.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Template e padroes de design para criar paginas HTML de cursos no formato INEMA.CLUB COM camada de aprendizagem por cima — progresso/marcar-lido, duvida, anota… |
| Entradas (gatilhos) | minha jornada, formato de curso, template de curso |
| Ferramentas citadas | flux, hyperframes, node |
| Processo (cabeçalhos) | Formato Curso v2 - INEMA.CLUB (com camada de aprendizagem) → Referencias → Arquivos da camada de aprendizagem (assets/) → Fluxo de Trabalho → 1. Entender o que sera criado → 2. Ler o MASTER_COMPLETO.md → 3. Criar a pagina seguindo os templates do MASTER → 4. Verificar com CHECKLIST_REVISAO.md → Imagens geradas com inemaimg (complementar) → Modelos e licenca (importante) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 30,149 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/learn.js`

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
