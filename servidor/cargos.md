# Cargos

Os cargos do servidor são grupos do LuckPerms. A maioria vem do Discord: o
Simple Discord Link dá o grupo de quem tem o cargo correspondente lá. Os nós
de permissão e os comandos da staff ficam nas configs, que são privadas.

## Hierarquia

A escada da staff (*track* `staff`) sobe nesta ordem. Cada degrau herda o que
o anterior pode.

| Grupo | Prefixo | Papel | Vem do Discord |
| --- | --- | --- | --- |
| `miner` | `MNR` | Jogador verificado | cargo Autenticado |
| `support` | `SPR` | Suporte aos jogadores | cargo Support |
| `moderador` | `MOD` | Moderação | a sincronizar |
| `dev` | `DEV` | Administração técnica | a sincronizar |
| `owner` | `OWN` | Donos do servidor | cargo Owners |

Fora da escada, estes herdam do `miner` e só mudam o prefixo e alguns extras:

| Grupo | Prefixo | Vem do Discord |
| --- | --- | --- |
| `booster` | `BST` | cargo Server Booster |
| `apoiador` | `APO` | a sincronizar |
| `builder` | `BDR` | cargo Building |

**A definir:** o cargo Ajudante do Discord ainda não tem grupo no LuckPerms
(posição na escada e comandos em aberto), e os cargos Apoiador, Moderador e
Dev ainda não foram criados no Discord.

## Comandos do jogador

O que todo jogador verificado (`miner`) pode usar, pela raiz do comando:

| Assunto | Comandos |
| --- | --- |
| Conta | `/register`, `/login`, `/logout`, `/account`, `/discordverify` |
| Teletransporte | `/spawn`, `/home`, `/warp`, `/back`, `/rtp`, `/tpa`, `/tpahere`, `/tpaccept`, `/tpdeny`, `/tpcancel` |
| Terrenos | `/flan` |
| Conversa | `/msg`, `/tell`, `/w`, `/voicechat`, `/emotes` |
| Comércio | `/lcterminal`, `/lctrade`, `/lctradeaccept`, `/lcbaltop` |
| Utilidades | `/enderchest`, `/workbench`, `/anvil`, `/grindstone`, `/stonecutter`, `/wastebin`, `/starterkit` |
| Outros | `/skin`, `/sk`, `/plstyle`, `/pet`, `/open`, `/jm`, `/ponder`, `/guideme`, `/suicide` |

Comando novo de mod começa negado para todos até alguém liberar.

A lista sai dos grupos `default` e `miner` das configs. Quando eles mudarem,
atualize esta página.
