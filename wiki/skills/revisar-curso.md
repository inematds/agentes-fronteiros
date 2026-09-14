---
type: Skill
title: revisar-curso
description: Audita e corrige paginas HTML de cursos no formato INEMA.CLUB. Use esta skill SEMPRE que o usuario pedir para revisar, auditar, checar ou validar um curso existente. Acione quando o usuario
  mencionar "revisar curso", "c…
resource: file:///home/nmaldaner/.claude/skills/revisar-curso/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/revisar-curso/SKILL.md
  author: human:nei
  last_modified: '2026-05-17'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/curso
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - flux
  gatilhos:
  - revisar curso
  - checar paginas
  - verificar consistencia
  - auditar trilhas
  tamanho_skill_md: 10689
migracao:
  estagio: inventariado
  cluster: curso
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# revisar-curso

## Descrição (do SKILL.md)

Audita e corrige paginas HTML de cursos no formato INEMA.CLUB. Use esta skill SEMPRE que o usuario pedir para revisar, auditar, checar ou validar um curso existente. Acione quando o usuario mencionar "revisar curso", "checar paginas", "verificar consistencia", "auditar trilhas" ou qualquer pedido de revisao de qualidade em paginas HTML de curso. NAO use para criar paginas novas (use formato-curso para isso).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Audita e corrige paginas HTML de cursos no formato INEMA.CLUB. Use esta skill SEMPRE que o usuario pedir para revisar, auditar, checar ou validar um curso exis… |
| Entradas (gatilhos) | revisar curso, checar paginas, verificar consistencia, auditar trilhas |
| Ferramentas citadas | flux |
| Processo (cabeçalhos) | Revisar Curso - Auditoria INEMA.CLUB → Fluxo de Execucao → Etapa 1 - Inventario → Etapa 2 - Consistencia de Navegacao → Etapa 3 - Sistema de Cores → Etapa 4 - Light Mode (CRITICO) → Etapa 5 - Conteudo e Componentes → Etapa 6 - Profundidade dos Modulos (CRITICO) → Etapa 7 - Relatorio → Comandos de busca uteis para a auditoria |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 10,689 chars |

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
