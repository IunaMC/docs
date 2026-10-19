# Propagar uma estável

Depois de uma estável do `modpack`, leve a mesma versão ao pack da staff e às
configs. No Claude Code, a skill `/propagar` do modpack faz estes passos, e o
`/estavel` já a chama no fim.

## Moderação

1. O workflow *Acompanhar pack base* do `modpack-moderacao` abre a branch
   `base/vX.Y.Z`. Ele roda todo dia; para não esperar:
   `gh workflow run acompanhar-base.yaml -R IunaMC/modpack-moderacao`.
2. O commit do bot vem sem assinatura. Faça checkout da branch, rode
   `git commit --amend --no-edit --reset-author -S -s` e
   `git push --force-with-lease`.
3. Abra o PR para a `main` e, com o Validar verde, faça merge com `--merge`.
4. Alinhe a `devel/devel` de lá: `git fetch`, `git merge --ff-only origin/main`
   e `git push`.

## Configs

1. No `minecraft-config`, na `devel/devel`, escreva a versão em `MODPACK`
   (sem o `v`).
2. Commit `build: testa com o modpack X.Y.Z` e push.
3. Publique a versão das configs pelo processo de lá (`VERSAO` +
   `MUDANCAS.md`, documentado no `docs/versoes.md` daquele repositório). O
   Release dele sobe o servidor com o pack novo antes de publicar.

Depois disso, falta o [envio das configs ao servidor](enviar-configs.md).
