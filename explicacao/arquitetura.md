# Arquitetura

O IUNA é um modpack de Minecraft 1.21.1 com NeoForge, mantido como código e
entregue de forma automática a três destinos: o launcher do jogador, as
plataformas (Modrinth e CurseForge) e o servidor.

```text
            ┌──────────────────── IunaMC/modpack ─────────────────────┐
 mod novo ─►│ pack/ (packwiz)  ──push──►  CI: Validar  ──►  Release   │
            │ um .pw.toml por mod          README, hashes,   tag, .mrpack,
            │ side = client/server/both    CurseForge,       .zip, notas
            │                              servidor sobe     │
            └────────────────────────────────────────────────┼────────┘
                                                             │
          ┌──────────────────────┬───────────────────────────┼──────────────────┐
          ▼                      ▼                           ▼                  ▼
   GitHub Releases          Modrinth                    CurseForge        servidor (a cada boot)
   (.mrpack, iuna.club/    (página em modrinth/,       (.zip completo,   packwiz-installer
    mrpack)                  versões pelo Release)       revisão manual)   ← iuna.club/pack/pack.toml
                                                                            ← main (só estáveis)
```

## As peças

**Pack como código.** O `pack/` do `modpack` não tem nenhum jar: cada mod é
um `.pw.toml` com a origem (Modrinth e, para o cliente, também a CurseForge),
o hash e o lado (`client`, `server`, `both`). O `index.toml` guarda o hash de
cada arquivo. O mesmo pack serve ao jogador e ao servidor
([decisão do modpack](https://github.com/IunaMC/modpack/blob/main/docs/decisoes/0001-packwiz-fonte-unica.md)).

**Integração contínua.** Todo push fora da `main` que mexe no pack roda o
*Validar*: confere a lista de mods do README, a fonte da CurseForge e os
hashes, exporta os artefatos e sobe um servidor de verdade com as configs do
`minecraft-config`. A estável só vai para a `main` com o Validar verde na
`devel/devel`.

**Entrega.** O *Release* lê a versão do `pack/pack.toml` (SemVer). Na
`devel/devel`, beta sai como *pre-release*. Na `main`, que só recebe PR com
merge commit, sai a estável. Ele cria a tag, a release com o `.mrpack` e as
notas do `MUDANCAS.md` e publica no Modrinth e na CurseForge.

**Servidor.** A cada boot, o servidor roda o `packwiz-installer` contra
`https://iuna.club/pack/pack.toml`, um atalho que redireciona para o pack da
`main`. Ele baixa só o que é `server` e `both` e apaga o que saiu do pack. Como
a `main` só tem estáveis, reiniciar é o deploy
([decisão 0002](../decisoes/0002-servidor-instala-da-main.md)). As configs vêm
do `minecraft-config` por um envio manual
([processo](../processo/enviar-configs.md)).

**Pack da staff.** O `modpack-moderacao` herda o pack pelo `base.toml` e soma
os mods de moderação. Uma estável nova abre a atualização de lá sozinha
([propagar](../processo/propagar.md)).

**Rotina automática.** Toda segunda, o `modpack` abre uma issue com os mods
que têm versão nova e outra com o resumo do estado dos três repositórios. O
Dependabot atualiza as actions dos workflows.

## Atalhos do domínio

| Atalho | Leva a |
| --- | --- |
| `https://iuna.club/modpack` | Página do pack no Modrinth |
| `https://iuna.club/mrpack` | `.mrpack` da última release |
| `https://iuna.club/pack/pack.toml` | `pack/pack.toml` da `main`, para o instalador do servidor. O `index.toml` e os `.pw.toml` resolvem no mesmo caminho |

São redirecionamentos simples, mantidos à mão no DNS.

## Onde cada coisa está documentada

- Comandos do dia a dia do pack: [`docs/` do modpack](https://github.com/IunaMC/modpack/tree/main/docs).
- O que atravessa repositórios: o [ciclo de versão](../processo/ciclo-de-versao.md)
  e as outras páginas de [processo](../SUMMARY.md#processo).
- Os nomes técnicos de cada peça: o [glossário](glossario.md).
