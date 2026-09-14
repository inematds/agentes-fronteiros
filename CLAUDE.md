# agentes-fronteiros — regras do projeto

## O que é
Projeto de migração: agentes especializados → agente generalista + skills com contrato + tools + loop + wiki (OKF). Ler `README.md`, depois `PLANO.md` e `ARQUITETURA.md`.

## Conta git
Repo da conta **inematds** → autor/committer `inematds <inematds@gmail.com>`.

## Wiki (`wiki/`) — regras de manutenção
- É um bundle **OKF**: todo `.md` fora `index.md`/`log.md` é conceito e precisa de `type` no frontmatter. Convenções em `wiki/SCHEMA.md`.
- Fonte bruta entra em `wiki/raw/AAAA-MM-DD-<slug>.md` e **não é editada**. O conceito curado aponta pra ela em `sources`.
- Quem gera/edita um conceito preenche `generated: {by, at}`. Revisão humana entra em `verified`.
- Fato desatualizado: marcar `status: deprecated` ou seção "Superado" — não apagar.
- Toda alteração relevante ganha uma linha em `wiki/log.md` (mais recente no topo).
- Antes de commitar: `python3 tools/wiki_lint.py` tem que passar.

## Páginas de skill (`wiki/skills/*.md`) e estado de migração
- Geradas por `python3 tools/inventario.py` a partir de `~/.claude/skills` e `~/.claude/agents`. Rodar de novo sempre que uma skill for criada/removida.
- O gerador **preserva** o campo `migracao:` e a seção `## Notas de migração`. Todo o resto é sobrescrito.
- O estágio de migração só muda via interface (`interface/server.py`) ou editando o frontmatter — não criar arquivo de estado paralelo.

## Contratos
- Um por skill migrada, em `migracao/contratos/<nome>.yaml`, seguindo `migracao/template-contrato.yaml`. Campos: `trigger`, `input`, `output`, `tools`, `acceptance`, `loop`.
- A skill migrada em `agent/skills/<nome>/` copia o contrato como `contrato.yaml` ao lado do `SKILL.md`.

## Interface
`python3 interface/server.py` → http://127.0.0.1:8765. Só stdlib + PyYAML. Não adicionar framework.

## Falhas
Registrar em `FALHAS.md` (uma linha por falha, formato do CLAUDE.md global).
