# docs

Documentação que atravessa os repositórios da IunaMC (decisão 0003). Siga o `referencia/padrao-de-escrita.md` e o `CONTRIBUTING.md`; página nova entra no `SUMMARY.md`.

- **Branches:** trabalho na `docs/docs`, PR para a `main` com merge commit (`gh pr merge --merge`). Nunca rebase-merge: recria os commits sem assinatura.
- **Regras do Claude:** o texto oficial é `referencia/claude.md`. Mudou? Rode `python3 scripts/regras-comuns.py sincronizar` nos quatro repositórios (`../iunamc.docs`, `../iunamc.modpack`, `../iunamc.modpack-moderacao`, `../iunamc.minecraft-config`).

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
