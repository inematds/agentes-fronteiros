---
name: <nome>
version: 0.1.0
description: <o que faz> + Use quando <frases do usuário, entre aspas>. NÃO use para <cluster vizinho>.
---

# <Nome da skill>

## Objetivo
Uma frase.

## Quando usar / quando não usar
- Usar: …
- Não usar: … (apontar a skill certa)

## Entradas
Ver `contrato.yaml` → `input`. Confirmar obrigatórios antes de começar.

## Saídas esperadas
Ver `contrato.yaml` → `output`. Um arquivo por formato, em `~/projetos/output/<projeto>/`.

## Processo
1. …
2. …
(Só o esqueleto. Detalhe em `references/` — carregar apenas o necessário.)

## Ferramentas permitidas
Ver `contrato.yaml` → `tools`. Executar `agent/tools/*`, nunca reescrever.

## Regras
- …

## Critérios de qualidade
Ver `contrato.yaml` → `acceptance`.

## Loop
planejar → executar → inspecionar (`<o que abrir>`) → criticar contra `acceptance` → corrigir → testar (`<validador>`). Teto: 3 voltas.

## Processo de validação
Comando(s) que provam a entrega. Se falhar 3×: entregar rascunho + dizer o que falhou + `FALHAS.md`.

## References
- `references/estilo.md` — …
- `references/exemplos.md` — …
