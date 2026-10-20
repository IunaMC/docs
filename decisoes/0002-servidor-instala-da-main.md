# 0002: o servidor instala da `main`

- **Data:** 16/10/2026; atalho do domínio em 18/10/2026
- **Estado:** aceita
- **Origem:** `IunaMC/modpack@5139593` (pack como fonte única do cliente e do
  servidor) e `IunaMC/modpack@5c5633b` (betas pela `devel/devel`, só estáveis
  pela `main`)

## Contexto

Antes, os mods do servidor eram mantidos à parte (`modpack-servidor`) e
enviados à mão. O pack do jogador e o do servidor podiam divergir sem ninguém
perceber.

## Decisão

O servidor roda o `packwiz-installer-bootstrap` com `-s server` a cada boot,
contra o `pack/pack.toml` da `main` do `modpack`, pelo atalho
`https://iuna.space/pack/pack.toml`. A `main` só recebe versões estáveis: o
Release recusa beta nela e falha se o `pack/` mudar sem versão nova.

## Consequências

- Reiniciar o servidor é o deploy do pack. Não há passo manual para os mods.
- Beta nunca chega à produção, porque sai da `devel/devel`.
- O atalho permite trocar a origem sem mexer no comando do painel.
- O servidor depende do GitHub no boot
  ([contingência](../processo/se-o-github-cair.md)).
- Fixar uma versão exige trocar o comando para a URL do GitHub com a tag.
- As configs não seguem o mesmo caminho: são enviadas à mão
  ([processo](../processo/enviar-configs.md)).

## Notas

- *Nota de 20/10/2026:* o iuna.space expirou, e o atalho passou a ser
  `https://iuna.club/pack/pack.toml`, com o mesmo redirecionamento. A decisão
  não mudou ([migrar o domínio](../processo/migrar-dominio.md)).
