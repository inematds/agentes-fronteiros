# Plano de migração — agentes especializados → agente generalista + skills

Fonte bruta: `wiki/raw/2026-09-14-plano-migracao-agentes-skills.md` (texto original, intocado).
Esta é a versão **operacional**: o mesmo plano, com o que cada etapa produz neste repositório.

## Tese

> Não precisamos criar mais agentes. Precisamos ensinar agentes gerais a trabalhar do nosso jeito.

A lógica muda de **agentes especializados e isolados** para:

**agente generalista → skills especializadas → ferramentas reutilizáveis → loops de verificação → aprendizado contínuo**

Fórmula resumida: **INTENÇÃO → CONTEXTO → SKILL → FERRAMENTAS → LOOP → APRENDIZADO**

## As 10 etapas e o que produzem aqui

| # | Etapa | Produz | Onde |
|---|---|---|---|
| 1 | Inventariar | Agente → tarefa → entradas → ferramentas → processo → saída → validação, por skill/agente. Detectar repetição. | `tools/inventario.py` → `wiki/skills/*.md`, `wiki/agentes/*.md`, `wiki/clusters/*.md` |
| 2 | Agente base | Um agente geral que sabe usar arquivos, terminal, web, MCP, APIs, memória e skills. | `agent/instructions.md`, `agent/agent.yaml` |
| 3 | Agentes → skills | Cada agente vira skill com: objetivo, quando usar, entradas, saídas, processo, ferramentas permitidas, regras, critérios de qualidade, validação. | `migracao/template-SKILL.md` → `agent/skills/<nome>/SKILL.md` |
| 4 | Código repetido → tools | ffmpeg, render, thumbnail, download, transcrição, validação como ferramentas prontas. | `agent/tools/` |
| 5 | Progressive disclosure | `SKILL.md` enxuto + `references/`, `scripts/`, `templates/` carregados sob demanda. | estrutura de cada skill migrada |
| 6 | Correção → aprendizado | Corrigir o sistema, não a saída: skill / regra / exemplo / script. Registrar em `FALHAS.md` e na wiki (`log.md`). | `FALHAS.md`, `wiki/log.md`, `wiki/conceitos/aprendizado-permanente.md` |
| 7 | Loop dentro da skill | PLANEJAR → EXECUTAR → INSPECIONAR → CRITICAR → CORRIGIR → TESTAR → passou? A 1ª versão é rascunho. | seção "Loop" em cada SKILL.md; `wiki/conceitos/loop-de-validacao.md` |
| 8 | Contrato da skill | trigger, input, output, tools, acceptance em YAML. | `migracao/template-contrato.yaml`, `migracao/contratos/*.yaml` |
| 9 | Router | Agente identifica a intenção e escolhe a skill; nome + descrição precisam ser claros. | `agent/instructions.md` (seção Router) reaproveitando `maestro-roteador` e `diretor-ecossistema` |
| 10 | Sistema vivo | Executa → verifica → critica → loop → entrega → aprende → atualiza skill. | tudo junto; wiki como memória operacional |

## Estratégia prática (não migrar tudo de uma vez)

Começar por **3**: `reels`, `video-explicativo`, `curso`. Para cada um:

1. mapear o processo atual (página em `wiki/skills/`, estágio `mapeado`);
2. transformar o processo em skill (`agent/skills/<nome>/SKILL.md`, estágio `skill`);
3. mover código repetido para `agent/tools/` (estágio `tools`);
4. definir entradas e saídas + 5. critérios de aceitação (`contrato.yaml`, estágio `contrato`);
6. adicionar loop de validação (estágio `loop`);
7. testar em tarefas reais (`evals/tarefas/`, estágio `testado`);
8. corrigir a skill quando houver falha (`FALHAS.md`);
9. aprovar e usar o padrão nos demais (estágio `aprovado`).

Os estágios acima são exatamente os valores do campo `migracao.estagio` no frontmatter de cada página em `wiki/skills/`, que a interface (`interface/`) mostra como kanban.

## Ordem sugerida depois dos pilotos

1. Clusters com mais sobreposição primeiro (ver `wiki/clusters/`): onde 3+ skills disputam a mesma intenção, o ganho de consolidar é maior.
2. Famílias com prefixo (`comfy-*`, `hyperframes-*`, `printing-press-*`, `inemaref-*`): viram **uma** skill com `references/` por subtema, ou permanecem como sub-skills de uma skill-mãe.
3. Skills utilitárias (clima, design-dna, theme-factory…): ficam como estão, só ganham contrato.
4. Agentes do Conselho (`mestre-do-conselho` + 3 membros): permanecem como subagentes (`agent/subagents/`), pois precisam de contexto isolado por desenho.

## Resultado esperado

```text
Agentes especializados → Agente generalista → Skills especializadas →
Ferramentas reutilizáveis → Validação automática → Loops de melhoria →
Aprendizado operacional permanente
```
