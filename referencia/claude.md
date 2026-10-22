# Regras do Claude Code

Regras que valem em todos os repositórios da IunaMC. O Claude Code só lê o
`CLAUDE.md` da pasta onde a sessão começa, então cada repositório leva uma
cópia literal do bloco abaixo. O texto oficial é este; não edite a cópia.

## Como a cópia funciona

- O bloco fica entre os dois comentários `regras-comuns:inicio` e
  `regras-comuns:fim`, no `CLAUDE.md` de cada repositório. As regras
  específicas do repositório ficam fora dele.
- Para mudar uma regra comum, edite este arquivo e rode, a partir daqui,
  `python3 scripts/regras-comuns.py sincronizar <caminho dos repositórios>`.
  Depois abra um PR em cada repositório.
- O job *Regras do Claude* de cada repositório baixa este arquivo e o script
  da `main` e roda `conferir`. Ele recusa o PR se o bloco divergir.

<!-- regras-comuns:inicio -->
## Regras comuns da IunaMC

Texto oficial em
[IunaMC/docs](https://github.com/IunaMC/docs/blob/main/referencia/claude.md).
Não edite este bloco: mude lá e rode `scripts/regras-comuns.py sincronizar`.

- **Commits:** `git commit -S -s`, [Conventional Commits](https://www.conventionalcommits.org/pt-br/) em português. Nunca `Co-Authored-By` nem menção ao Claude, nem em commit, PR, issue ou release.
- **Idioma:** português do Brasil em código comentado, documentação, commits, PRs e issues. A única exceção é a página do Modrinth, em inglês com o português recolhível.
- **Repositório público:** nada de host, hardware, IP, DNS interno, caminho local nem segredo. Isso fica nos repositórios privados, e a página pública só diz que existe.
- **Uma sessão por tarefa:** tarefa sem relação com a anterior abre sessão nova, porque o histórico é reenviado a cada mensagem.
- **Antes de perguntar ao usuário:** leia a memória, o `git log` e as sessões anteriores. Pergunte só o que não estiver registrado.
- **Modelo e esforço:** a skill fixa o modelo no cabeçalho; sem skill, siga a tabela. Em subagente, passe o `model` dela.

  | Tarefa | Modelo | Esforço |
  | --- | --- | --- |
  | Mecânica: commit, mover arquivos, atualizar notas, conferir o CI | Haiku ou Sonnet | baixo |
  | Rotina com algum julgamento: revisar config, escrever guia | Sonnet | médio |
  | Decisão de projeto, depuração, análise de crash | Opus | alto |
<!-- regras-comuns:fim -->
