# agent/subagents/ — agentes com contexto isolado

Só o que precisa de isolamento por desenho. Hoje (de `~/.claude/agents`):

- `mestre-do-conselho` + `advogado-do-diabo` · `analista-neutro` · `estrategista-otimista` — Conselho de Agentes.
- `diretor-ecossistema` — roteador de ferramenta de vídeo (absorvido pelo Router; pode permanecer como subagente enquanto a tabela não cobrir tudo).
- `web-research-assistant` — pesquisa web.
- `triple-x-responder` — placeholder; candidato a descontinuar.

Regra eve: subagente **não herda** instruções/tools/skills da raiz. O que ele precisa vai na pasta dele ou em `lib/`.
