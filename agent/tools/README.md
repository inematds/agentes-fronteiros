# agent/tools/ — ferramentas reutilizáveis (etapa 4)

Código que hoje se repete entre skills. A skill **manda executar**, não reescreve.

Contrato de cada tool: CLI com argumentos nomeados, saída JSON em stdout, exit 0/1, `--help` funcionando.

Candidatas detectadas pelo inventário (ver `wiki/clusters/*.md`, seção "Repetição detectada"):

| Tool | Substitui | Fonte provável |
|---|---|---|
| `download_video.py` | yt-dlp avulso em várias skills | `~/projetos/inemavox/baixar_v1.py` |
| `transcribe.py` | Whisper/Groq refeito em reels, video-explicativo, dublagem | `~/projetos/inemavox/transcrever_v1.py` + Groq |
| `render_video.py` | render HyperFrames/pixflow chamado de N jeitos | skills hyperframes-cli / pixflow-motion |
| `extract_audio.py` · `create_thumbnail.py` | ffmpeg inline | — |
| `validate_video.py` | checagem de duração, aspect, áudio, texto cortado | acceptance dos contratos |
| `tts.py` | narração inemavox (chatterbox/rachel) | `~/projetos/inemavox` |

Nada aqui é implementado ainda: a ordem é migrar o piloto, ver o que se repete de fato, e só então extrair.
