# 0001: repositórios separados por papel

- **Data:** 16/10/2026
- **Estado:** aceita
- **Origem:** criação do `modpack` em packwiz (`IunaMC/modpack@44212fe`) e
  arquivamento do `modpack-servidor`

## Contexto

O pack, as configs do servidor, o pack da staff e a infraestrutura têm
públicos, ritmos e níveis de sigilo diferentes. O pack é público e muda a cada
mod. As configs guardam marcadores de segredos (token do bot, IDs do Discord)
e mudam com o balanceamento. O pack da staff soma mods de moderação ao pack
dos jogadores. A infraestrutura descreve o host.

## Decisão

Um repositório por papel ([lista](../referencia/repositorios.md)): `modpack`
público como fonte única do pack, `minecraft-config`, `modpack-moderacao` e
`minecraft-infra` privados. Eles se ligam por versão: o `base.toml` da
moderação e o `MODPACK` das configs apontam para uma tag do `modpack`.

## Consequências

- Cada repositório tem CI, versão e changelog próprios.
- Uma estável do `modpack` precisa ser propagada aos outros
  ([propagar](../processo/propagar.md)), em parte por automação (Acompanhar
  pack base) e em parte por commit.
- A documentação que atravessa repositórios precisou de um lugar próprio
  ([0003](0003-documentacao-em-repo-proprio.md)).
