# evals/ — tarefas reais que aprovam uma skill migrada

Irmão de `agent/` (regra eve). Uma tarefa por arquivo em `tarefas/`, com: pedido literal do usuário, entrada, skill esperada pelo router, `acceptance` do contrato a verificar, resultado.

Uma skill só sobe para `migracao.estagio: testado` depois de passar em ≥ 2 tarefas daqui, e para `aprovado` depois de uso real sem correção.
