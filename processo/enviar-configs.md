# Enviar as configs ao servidor

Uma release do `minecraft-config` fica pronta no GitHub, mas só vale no jogo
depois que alguém envia as configs ao servidor. Este passo é manual, e o
passo a passo detalhado fica no `docs/enviar-ao-servidor.md` do
`minecraft-config` (privado).

## Em resumo

1. Antes de tudo, baixe do servidor os arquivos do Simple Discord Link que têm
   o token e os IDs do Discord.
2. Troque a pasta `config/` inteira pela do `.zip` da release.
3. Preencha os marcadores `{{NOME}}` com os valores baixados no passo 1.
4. Reinicie o servidor pelo painel.

**Nunca apague `world/`.**

## Acompanhamento

O GitHub não tem como saber se o envio aconteceu. Por isso, cada release das
configs abre no `minecraft-config` a issue **Enviar configs X.Y.Z ao
servidor** (etiqueta `envio`), com os passos em checklist. **Feche-a depois de
enviar.** Uma versão nova fecha a anterior que não chegou a ser enviada, e o
Resumo semanal do `modpack` lista as que estão abertas.

Para abrir uma à mão, no `minecraft-config`:

```sh
bash .github/scripts/issue-envio.sh X.Y.Z
```
