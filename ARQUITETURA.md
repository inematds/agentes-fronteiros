# Arquitetura

## 1. Modelo de pastas: eve (Vercel) como convenção

O eve é um framework *filesystem-first*: o agente é um diretório, e cada
capacidade é um arquivo em um *slot* nomeado. Adotamos **os nomes dos slots e
a regra "os arquivos são a interface"**, mas o runtime continua sendo o Claude
Code (skills, agentes `.md`, MCP, hooks). Nada aqui pretende compilar com `eve build`.

| Slot eve (`agent/…`) | O que é no eve | Equivalente aqui (Claude Code) |
|---|---|---|
| `agent.ts` | modelo + config de runtime | `agent/agent.yaml` (modelo, esforço, política de roteamento) |
| `instructions.md` | system prompt sempre ligado (obrigatório) | `agent/instructions.md` — o INEMA AGENT generalista; alimenta `CLAUDE.md`/prompt base |
| `skills/<x>.md` | procedimento carregado sob demanda via `load_skill` | `agent/skills/<x>/SKILL.md` — a ferramenta Skill do Claude Code |
| `tools/<x>.ts` | função tipada que o modelo chama | `agent/tools/<x>.py` — script pronto executado via Bash (contrato de CLI + JSON) |
| `connections/` | MCP e serviços externos | `agent/connections/*.md` — lista de MCPs em uso (magnific, metricool, chrome…) |
| `channels/` | por onde chega mensagem (Slack, HTTP…) | `agent/channels/*.md` — terminal, Telegram (inemaccbot), API do inemavox |
| `schedules/` | cron | `agent/schedules/*.md` — rotinas (/loop, /schedule, cron) |
| `subagents/<id>/` | agente filho com slots próprios e contexto isolado | `agent/subagents/<id>.md` — os `.md` de `~/.claude/agents` (Conselho etc.) |
| `hooks/` | ganchos do ciclo de vida | `agent/hooks/` — hooks de `settings.json` |
| `lib/` | helpers compartilhados | `agent/lib/` — módulos Python usados por várias tools |
| `sandbox/` | workspace semeado | `agent/sandbox/` — pasta de saída padrão (`~/projetos/output`) e fixtures |
| `evals/` (irmão de `agent/`) | testes de comportamento | `evals/tarefas/*.md` — tarefas reais que aprovam uma skill migrada |

Regras herdadas do eve que valem aqui:

- **A descrição da skill é dica de roteamento, não rótulo.** Escrever como a tarefa que dispara ("Use quando o usuário pedir X").
- **Carregar skill acrescenta instruções, não uma nova superfície de execução.** Comportamento tipado vai para `tools/`.
- **Subagente declarado não herda nada da raiz.** Se dois subagentes precisam do mesmo procedimento, duplica-se o markdown ou compartilha-se via `lib/`.

## 2. Base de conhecimento: OKF + LLM wiki

### 2.1 OKF (Open Knowledge Format)

A pasta `wiki/` é um **bundle OKF**: árvore de `.md` com frontmatter YAML.

- Todo `.md` que não seja `index.md` ou `log.md` é um **conceito**; o *concept ID* é o caminho sem `.md`.
- `type` é o **único campo obrigatório**. Os outros vêm das famílias do spec:
  - identidade: `title`, `description`, `resource`, `tags`
  - proveniência: `sources` (lista de `{path|url, author, last_modified…}`)
  - confiança: `generated: {by, at}`, `verified: [{by, at}]` → *trust tier* derivada (não verificado / confirmado por máquina / revisado por humano)
  - ciclo de vida: `status: draft|stable|deprecated`, `stale_after`
- Atores: `human:<id>`, `<produtor>/<versão>` para agentes, `process:<id>` para processos.
- Consumidores **toleram campos desconhecidos**: usamos isso para o campo `migracao:` nas páginas de skill.

Detalhe completo das convenções: `wiki/SCHEMA.md`.

### 2.2 LLM wiki (estilo Karpathy)

A wiki não é escrita à mão: **o agente a mantém**. Padrão de operação:

1. **Ingerir** — fonte bruta entra em `wiki/raw/` com data no nome. Nunca é editada.
2. **Consolidar** — o agente lê a fonte, atualiza ou cria conceitos em `wiki/conceitos/`, `wiki/skills/`, `wiki/agentes/`, `wiki/clusters/`, preenche `sources` apontando para o raw, marca `generated.by`.
3. **Indexar** — regenera `index.md` de cada pasta (listagem com uma linha por conceito).
4. **Registrar** — acrescenta uma linha em `log.md` (o quê, quando, por quem).
5. **Consultar** — perguntas ao sistema passam primeiro por `index.md` (barato) e só depois abrem conceitos (progressive disclosure).
6. **Lint** — `tools/wiki_lint.py` falha se faltar `type`, se houver link quebrado ou nome reservado usado como conceito.

O mesmo mecanismo do `cerebro-vip` (páginas por entidade, `fontes` como backlinks imutáveis, `relacionados` como arestas, "superado" em vez de apagar) é aplicado aqui com os nomes de campo do OKF.

## 3. Ciclo do agente generalista

```text
PEDIDO
  ↓ (router: intenção → cluster → skill; usa maestro-roteador p/ modelo/esforço)
SKILL (SKILL.md + contrato.yaml)
  ↓ carrega só references/ necessários
TOOLS (agent/tools/*.py) · MCP · APIs
  ↓
LOOP: planejar → executar → inspecionar → criticar → corrigir → testar
  ↓ passou nos `acceptance` do contrato?
ENTREGA
  ↓
APRENDIZADO: FALHAS.md (1 linha) + wiki/log.md + ajuste na skill/regra/exemplo/script
```

## 4. Estado de migração

Único lugar: frontmatter `migracao:` em `wiki/skills/<nome>.md`.

```yaml
migracao:
  estagio: inventariado   # inventariado|mapeado|skill|tools|contrato|loop|testado|aprovado|descontinuado
  cluster: reels          # id em wiki/clusters/
  destino: reels          # nome da skill migrada em agent/skills/ (quando houver)
  notas: ""               # texto livre
  atualizado: 2026-09-14
```

`tools/inventario.py` regenera as partes automáticas da página e **preserva** `migracao:` e a seção `## Notas de migração`. A interface lê e escreve esse campo via `interface/server.py`.
