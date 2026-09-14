# Plano de Migração para Agentes Generalistas + Skills

## Visão geral

A migração não exige abandonar os agentes atuais. A ideia é mudar a arquitetura para que o conhecimento operacional fique nas **Skills**, ferramentas reutilizáveis e processos de validação, em vez de ficar preso em agentes separados.

A lógica passa de:

**Agentes especializados e isolados**

para:

**Agente generalista → Skills especializadas → ferramentas reutilizáveis → loops de verificação → aprendizado contínuo**

---

## 1. Inventariar o que existe hoje

Para cada agente atual, mapear:

**Agente → tarefa → entradas → ferramentas → processo → saída → validação**

Exemplo:

**video-explicativo → recebe tema/documento → pesquisa → roteiro → imagens → vídeo → verifica duração/qualidade**

O objetivo é descobrir quais partes estão sendo repetidas entre agentes.

---

## 2. Criar um AGENTE BASE

Em vez de manter um agente separado para cada função:

- Agente vídeo
- Agente curso
- Agente pesquisa
- Agente reels
- Agente books

Criar um agente geral, por exemplo:

```text
JARVIS / INEMA AGENT
       ↓
 identifica intenção
       ↓
 escolhe SKILL
       ↓
 carrega contexto necessário
       ↓
 chama ferramentas
       ↓
 executa
       ↓
 valida
```

Esse agente base deve saber trabalhar com:

- arquivos
- terminal
- web
- MCP
- APIs
- memória
- Skills

---

## 3. Transformar agentes atuais em Skills

Exemplo de estrutura:

```text
skills/
├── video-explicativo/
├── curso/
├── reels/
├── heygen-avatar/
├── cria-books/
├── diretor-animacao/
└── videoprodutor/
```

Cada Skill deve ter, no mínimo:

```text
SKILL.md

Objetivo
Quando usar
Entradas
Saídas esperadas
Processo
Ferramentas permitidas
Regras
Critérios de qualidade
Processo de validação
```

---

## 4. Tirar código repetido das Skills

Se várias Skills ficam recriando scripts para:

- ffmpeg
- Python
- renderização
- thumbnails
- downloads
- transcrição

transformar isso em ferramentas reutilizáveis.

Exemplo:

```text
tools/
├── render_video.py
├── extract_audio.py
├── create_thumbnail.py
├── transcribe.py
├── download_video.py
└── validate_video.py
```

A Skill passa a mandar executar a ferramenta pronta, em vez de recriar código toda vez.

Exemplo:

```text
execute tools/render_video.py
```

em vez de:

```text
escreva novamente um programa Python para renderizar...
```

---

## 5. Criar Progressive Disclosure

Não colocar tudo dentro do `SKILL.md`.

Exemplo:

```text
video-explicativo/
│
├── SKILL.md
│
├── references/
│   ├── roteiro.md
│   ├── estilo-inema.md
│   ├── exemplos.md
│   └── formatos.md
│
├── scripts/
│   ├── render.py
│   └── validate.py
│
└── templates/
    └── video.json
```

O agente inicialmente lê apenas:

```text
nome
descrição
quando usar
```

Depois carrega apenas os arquivos realmente necessários para a tarefa.

---

## 6. Transformar correções em aprendizado permanente

Modelo atual:

```text
executa
↓
Nei vê erro
↓
Nei manda corrigir
↓
corrige
↓
fim
```

Novo modelo:

```text
executa
↓
erro identificado
↓
agente corrige
↓
investiga POR QUE errou
↓
decide onde corrigir
↓
Skill / regra / exemplo / script
↓
executa novamente
↓
valida
```

Princípio:

> Nunca corrigir apenas a saída. Corrigir o sistema que produziu a saída.

---

## 7. Colocar LOOP dentro das Skills

Modelo simples:

```text
INPUT
  ↓
PROCESSO
  ↓
OUTPUT
```

Novo modelo:

```text
INPUT
  ↓
PLANEJAR
  ↓
EXECUTAR
  ↓
INSPECIONAR
  ↓
CRITICAR
  ↓
CORRIGIR
  ↓
TESTAR
  ↓
passou?
 ↙    ↘
não    sim
 ↓      ↓
LOOP  ENTREGA
```

A primeira versão deixa de ser a entrega final e vira apenas um rascunho interno.

---

## 8. Definir contrato de cada Skill

Além de entrada e saída, cada Skill deve ter critérios de aceitação.

Exemplo:

```yaml
skill: reels

trigger:
  - criar reel
  - vídeo curto
  - short
  - vídeo vertical

input:
  tema: obrigatório
  publico: opcional
  duracao: 30-60s
  fonte: texto/url/video

output:
  formato: mp4
  aspect_ratio: 9:16
  duracao_max: 60s

tools:
  - web
  - image_gen
  - ffmpeg
  - tts

acceptance:
  - gancho <= 3 segundos
  - sem texto cortado
  - áudio sincronizado
  - fontes verificadas
  - duração <= 60s
```

Assim, a Skill funciona quase como uma função operacional da empresa.

---

## 9. Criar o ROUTER

O usuário não precisa dizer qual Skill deve ser usada.

O agente identifica a intenção e escolhe sozinho.

```text
PEDIDO
  ↓
ROUTER
  ↓
Qual é a intenção?
  ↓
┌────────┬─────────┬─────────┐
vídeo   curso     pesquisa   ...
 ↓        ↓          ↓
skill    skill      skill
```

Por isso, nome e descrição das Skills precisam ser muito claros.

---

## 10. Transformar tudo em um sistema vivo

Arquitetura sugerida:

```text
                 VOCÊ
                   │
             objetivo/intenção
                   ↓
          ┌─────────────────┐
          │ INEMA / JARVIS  │
          │ General Agent   │
          └────────┬────────┘
                   │
             INTENT ROUTER
                   ↓
             SKILL LIBRARY
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      VIDEO      CURSO     PESQUISA
        │          │          │
        └──────────┼──────────┘
                   ↓
              TOOL LAYER
      ┌────────────┼────────────┐
      ↓            ↓            ↓
     MCP          APIs        SCRIPTS
      ↓            ↓            ↓
             EXECUÇÃO
                 ↓
            VERIFICAÇÃO
                 ↓
             CRÍTICA
                 ↓
              LOOP
                 ↓
             ENTREGA
                 ↓
       APRENDE COM CORREÇÕES
                 ↓
           ATUALIZA SKILL
```

---

# Modelo arquitetural resumido

## INTENÇÃO → CONTEXTO → SKILL → FERRAMENTAS → LOOP → APRENDIZADO

Esse modelo permite transformar a forma de trabalhar com IA em um sistema operacional reutilizável.

---

## Estratégia prática de migração

Não migrar tudo de uma vez.

Começar com 3 agentes atuais:

1. `reels`
2. `video-explicativo`
3. `curso`

Para cada um:

1. mapear o processo atual;
2. transformar o processo em Skill;
3. mover código repetido para tools/scripts;
4. definir entradas e saídas;
5. criar critérios de aceitação;
6. adicionar loop de validação;
7. testar em tarefas reais;
8. corrigir a Skill quando houver falhas;
9. usar o padrão aprovado para os demais agentes.

---

# Resultado esperado

A evolução é:

```text
Agentes especializados
        ↓
Agente generalista
        ↓
Skills especializadas
        ↓
Ferramentas reutilizáveis
        ↓
Validação automática
        ↓
Loops de melhoria
        ↓
Aprendizado operacional permanente
```

A ideia central pode ser resumida assim:

> Não precisamos criar mais agentes. Precisamos ensinar agentes gerais a trabalhar do nosso jeito.
