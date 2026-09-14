---
type: Skill
title: generate
description: Gera imagem ou vídeo a partir de um prompt, roteando para a rota mais barata capaz (local/grátis primeiro, paga só quando o local não dá conta) e registrando o custo. NÃO use para editar vídeo
  já gravado, curso, landing…
resource: file:///home/nmaldaner/.claude/skills/generate/SKILL.md
tags:
- skill
- imagens
sources:
- path: /home/nmaldaner/.claude/skills/generate/SKILL.md
  author: human:nei
  last_modified: '2026-08-13'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/imagens
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 9
  subpastas:
  - models
  - references
  - scripts
  scripts:
  - scripts/gerar-local.py
  - scripts/registrar.py
  ferramentas:
  - flux
  - gemini
  - kling
  - pixflow
  - python
  gatilhos: []
  tamanho_skill_md: 5995
migracao:
  estagio: inventariado
  cluster: imagens
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# generate

## Descrição (do SKILL.md)

Gera imagem ou vídeo a partir de um prompt, roteando para a rota mais barata capaz (local/grátis primeiro, paga só quando o local não dá conta) e registrando o custo. NÃO use para editar vídeo já gravado, curso, landing ou avatar HeyGen.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Gera imagem ou vídeo a partir de um prompt, roteando para a rota mais barata capaz (local/grátis primeiro, paga só quando o local não dá conta) e registrando o… |
| Entradas (gatilhos) | — (extrair manualmente) |
| Ferramentas citadas | flux, gemini, kling, pixflow, python |
| Processo (cabeçalhos) | /generate → Pipeline → Roteamento → Portão de custo → Saída → Log → Scripts → imagem local (padrão) — gera, salva e loga em um passo → registrar um arquivo vindo de rota paga + lançar o custo no livro-caixa → quanto já gastei |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: models, references, scripts · SKILL.md com 5,995 chars |

## Scripts (candidatos a `agent/tools/`)

- `scripts/gerar-local.py`
- `scripts/registrar.py`

## Cluster

[imagens](../clusters/imagens.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
