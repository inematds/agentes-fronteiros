---
type: Skill
title: formato-curso-v5
description: 'curso INEMA v5 — página única (trilha + até 9 aulas), dark editorial com motor de retenção, feito para PÚBLICO ADULTO 40+ LEIGO, ocupado e profissional: promessa + tempo em toda aula, prática
  multi-modo SEM terminal (pr…'
resource: file:///home/nmaldaner/.claude/skills/formato-curso-v5/SKILL.md
tags:
- skill
- curso
sources:
- path: /home/nmaldaner/.claude/skills/formato-curso-v5/SKILL.md
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
  - assets/curso.js
  ferramentas:
  - node
  gatilhos:
  - formato de curso v5
  tamanho_skill_md: 13536
migracao:
  estagio: mapeado
  cluster: curso
  destino: curso
  notas: piloto 3 (v5) — contrato em migracao/contratos/curso.yaml
  atualizado: '2026-09-14'
---

# formato-curso-v5

## Descrição (do SKILL.md)

curso INEMA v5 — página única (trilha + até 9 aulas), dark editorial com motor de retenção, feito para PÚBLICO ADULTO 40+ LEIGO, ocupado e profissional: promessa + tempo em toda aula, prática multi-modo SEM terminal (prompt/tarefa/análise/código), linguagem sem jargão de plataforma, quadros escaneáveis, metáforas do mundo real e painel de jornada com progresso em capacidade. Use SEMPRE que o usuário pedir curso para leigos, curso 40+, curso INEMA.PRO, "formato de curso v5", curso sem vídeo para profissionais ocupados, curso de IA/automação/marketing para não técnicos, ou mencionar promessa/prática profissional/fundamento×ferramenta. NÃO use para curso técnico/dev com prática de código como centro — para esses, use a formato-curso-v4 (as duas coexistem).

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | curso INEMA v5 — página única (trilha + até 9 aulas), dark editorial com motor de retenção, feito para PÚBLICO ADULTO 40+ LEIGO, ocupado e profissional: promes… |
| Entradas (gatilhos) | formato de curso v5 |
| Ferramentas citadas | node |
| Processo (cabeçalhos) | Formato Curso v5 — INEMA (40+ leigo, dark editorial, retenção com portão de completude) → Leitura obrigatória → Protocolo de descoberta — Passo 0, bloqueante → Contrato de markup herdado (v4, íntegro — ver `formato-curso-v4/SKILL.md`) → Delta v5 — 9 componentes + 3 quadros (teto: 10 com contrato) → Contrato de conteúdo → Terceiro registro visual: `.termdemo` (demo real de comando) → Prática multi-modo → Limites numéricos → Checklist de aceitação (PORTÃO) |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: assets, references · SKILL.md com 13,536 chars |

## Scripts (candidatos a `agent/tools/`)

- `assets/curso.js`

## Cluster

[curso](../clusters/curso.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
