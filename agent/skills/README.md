# agent/skills/ — skills migradas

Cada skill migrada é uma pasta:

```text
<nome>/
├── SKILL.md          # enxuto: objetivo, quando usar, entradas, saídas, processo, ferramentas, regras, qualidade, validação, loop
├── contrato.yaml     # cópia de migracao/contratos/<nome>.yaml
├── references/       # carregado sob demanda (estilo, exemplos, formatos, gotchas)
├── scripts/          # só o que é específico da skill; utilitário genérico vai para agent/tools/
└── templates/
```

Template: `migracao/template-SKILL.md`. Enquanto a skill não é migrada, a versão em uso continua em `~/.claude/skills/<nome>/`.
