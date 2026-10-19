# Repositórios

Todos na organização [IunaMC](https://github.com/IunaMC). Os privados aparecem
aqui só pelo nome e pelo papel.

## Ativos

| Repositório | Visibilidade | Papel | Branches |
| --- | --- | --- | --- |
| [`modpack`](https://github.com/IunaMC/modpack) | público | Fonte única do pack, em packwiz. Jogador e servidor instalam daqui; `side = server` marca o que é só do servidor. Publica no Modrinth e na CurseForge. | `devel/devel` → `main` |
| `modpack-moderacao` | privado | Pack da staff: herda o `modpack` pelo `base.toml` e soma os mods de moderação. | `devel/devel` → `main` |
| `minecraft-config` | privado | `config/` e `server.properties` do servidor. O arquivo `MODPACK` diz com qual versão do pack elas foram testadas. | `devel/devel` → `main` |
| `minecraft-infra` | privado | Infraestrutura do servidor: compose, comando de inicialização e anotações. | `main` |
| [`docs`](https://github.com/IunaMC/docs) | privado até a revisão; depois, público | Esta documentação. | `main` |
| [`issues`](https://github.com/IunaMC/issues) | público | Bugs e sugestões da comunidade. | `main` |
| [`.github`](https://github.com/IunaMC/.github) | público | Perfil da organização e modelos de issue. | `main` |

## Arquivados

| Repositório | Visibilidade | Substituído por |
| --- | --- | --- |
| `modpack-servidor` | privado | `modpack`, quando o pack virou fonte única do jogador e do servidor (v3.0.0, 16/10/2026) |

## Dependências entre eles

- `modpack-moderacao` lê a tag do `modpack` em `base.toml`. O workflow
  *Acompanhar pack base* de lá abre a atualização quando sai uma estável.
- `minecraft-config` registra em `MODPACK` a versão do `modpack` com que foi
  testado. O Release de lá sobe o servidor com esse pack antes de publicar.
- O Validar do `modpack` clona o `minecraft-config` para subir o servidor
  com as configs. O Resumo semanal lê os três.

O passo a passo está no [ciclo de versão](../processo/ciclo-de-versao.md).
