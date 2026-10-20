# Propagar uma estável

Depois de uma estável do `modpack`, leve a mesma versão ao pack da staff e às
configs. No Claude Code, a skill `/propagar` do modpack faz estes passos, e o
`/estavel` já a chama no fim.

## Moderação

1. O workflow *Acompanhar pack base* do `modpack-moderacao` abre a branch
   `base/vX.Y.Z`. Ele roda todo dia; para não esperar:
   `gh workflow run acompanhar-base.yaml -R IunaMC/modpack-moderacao`.
2. O commit do bot vem sem assinatura. Refaça com a sua, no clone do
   `modpack-moderacao`:

   ```sh
   git fetch --prune && git switch base/vX.Y.Z
   ```

   ```sh
   git commit --amend --no-edit --reset-author -S -s && git push --force-with-lease
   ```

3. Abra o PR para a `main` e, com o Validar verde, faça merge com merge commit:

   ```sh
   gh pr create --base main --head base/vX.Y.Z --title "Pack base vX.Y.Z"
   ```

   ```sh
   gh pr merge <número> --merge
   ```

4. Alinhe a `devel/devel` de lá:

   ```sh
   git switch devel/devel && git fetch && git merge --ff-only origin/main && git push
   ```

## Configs

1. No clone do `minecraft-config`, na `devel/devel`, escreva a versão em
   `MODPACK` (sem o `v`):

   ```sh
   git switch devel/devel && git pull && echo X.Y.Z > MODPACK
   ```

2. Faça o commit e o push:

   ```sh
   git commit -S -s -am "build: testa com o modpack X.Y.Z" && git push
   ```

3. Publique a versão das configs pelo processo de lá (`VERSAO` +
   `MUDANCAS.md`, documentado no `docs/versoes.md` daquele repositório). O
   Release dele sobe o servidor com o pack novo antes de publicar.

Depois disso, falta o [envio das configs ao servidor](enviar-configs.md).
