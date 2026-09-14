# agent/connections/ — MCPs e serviços externos

| Conexão | Uso | Onde configurar |
|---|---|---|
| magnific (MCP) | imagem/vídeo/áudio/3D quando flux não der conta | Claude Code MCP; runbook `~/.claude/runbooks/magnific-modelos.md` |
| claude-in-chrome (MCP) | navegação/automação de páginas | extensão Chrome |
| metricool (MCP) | agendamento e métricas sociais | Claude Code MCP |
| context-mode (MCP) | processar saída grande fora do contexto | plugin |
| inemavox (HTTP :8010) | download, transcrição, TTS, música/SFX | `~/projetos/inemavox` |
| HeyGen (API) | avatar falante | key nos `.env` padrão |
| Groq (API) | Whisper rápido | key nos `.env` padrão |
