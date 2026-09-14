---
type: Skill
title: avatar-heygen-nei
description: Gera vídeo do avatar falante do Nei no HeyGen escolhendo entre os LOOKS/personagens dele (velho, beje, frio, índio, computador, quadro sol, quadro vermelho, afastado branco, FEP...). Use SEMPRE
  que o usuário pedir um ví…
resource: file:///home/nmaldaner/.claude/skills/avatar-heygen-nei/SKILL.md
tags:
- skill
- avatar
sources:
- path: /home/nmaldaner/.claude/skills/avatar-heygen-nei/SKILL.md
  author: human:nei
  last_modified: '2026-07-17'
generated:
  by: inventario.py/1.0.0
  at: '2026-09-14T17:24:22Z'
status: draft
related:
- clusters/avatar
skill:
  versao: ''
  invocacao_pelo_modelo: true
  arquivos: 1
  subpastas: []
  scripts: []
  ferramentas:
  - heygen
  - mcp
  - node
  gatilhos:
  - o nei índio
  - aquele do computador
  - o de quadro vermelho
  - o nei velho
  tamanho_skill_md: 3914
migracao:
  estagio: inventariado
  cluster: avatar
  destino: ''
  notas: ''
  atualizado: '2026-09-14'
---

# avatar-heygen-nei

## Descrição (do SKILL.md)

Gera vídeo do avatar falante do Nei no HeyGen escolhendo entre os LOOKS/personagens dele (velho, beje, frio, índio, computador, quadro sol, quadro vermelho, afastado branco, FEP...). Use SEMPRE que o usuário pedir um vídeo de avatar e mencionar um look/roupa/cenário/personagem ("o nei índio", "aquele do computador", "o de quadro vermelho", "o nei velho"), ou quando pedir um vídeo de avatar SEM dizer qual look — nesse caso LISTE os looks disponíveis e pergunte. Voz e engine são fixas (voz do .env, engine avatar_iii) a menos que o usuário peça diferente. Constrói por cima do heygen-cli.

## Mapa (etapa 1 do plano)

| Campo | Valor |
|---|---|
| Tarefa | Gera vídeo do avatar falante do Nei no HeyGen escolhendo entre os LOOKS/personagens dele (velho, beje, frio, índio, computador, quadro sol, quadro vermelho, af… |
| Entradas (gatilhos) | o nei índio, aquele do computador, o de quadro vermelho, o nei velho |
| Ferramentas citadas | heygen, mcp, node |
| Processo (cabeçalhos) | avatar-heygen-nei → Defaults travados (não perguntar, só aplicar) → Escolher o look → Gerar → Onde cada coisa mora → Privacidade dos IDs — regra dura → Notas de enquadramento |
| Saída | _preencher no mapeamento_ |
| Validação | _preencher no mapeamento_ |
| Progressive disclosure | subpastas: nenhuma · SKILL.md com 3,914 chars |

## Cluster

[avatar](../clusters/avatar.md)

## Notas de migração

_(vazio — a interface e o agente escrevem aqui)_
