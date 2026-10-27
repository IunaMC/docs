# Ciclo de versão

Como uma mudança no pack chega aos jogadores, à staff e ao servidor. Os
comandos de cada passo estão nos guias do modpack, linkados abaixo.

```text
mod novo ─► modpack devel/devel ─► beta (pre-release) ─► PR para main ─► estável
                                                                      │
              servidor de produção instala a main a cada boot ◄───────┤
                                                                      ├─► moderação (base.toml)
                                                                      └─► minecraft-config (MODPACK) ─► release ─► envio manual ao servidor
```

## 1. Mudar o pack

Na `devel/devel` do `modpack`, um commit por mod:
[adicionar](https://github.com/IunaMC/modpack/blob/main/docs/guias/adicionar-mod.md),
[remover](https://github.com/IunaMC/modpack/blob/main/docs/guias/remover-mod.md) ou
[atualizar](https://github.com/IunaMC/modpack/blob/main/docs/guias/atualizar-mods.md).
O Validar roda a cada push.

## 2. Beta

Sobe a versão no `pack/pack.toml` com sufixo `-beta.N`, reescreve o
`MUDANCAS.md` e faz push. O Release publica uma *pre-release* no GitHub e na
CurseForge. O servidor não a instala.
[Guia](https://github.com/IunaMC/modpack/blob/main/docs/guias/publicar-beta.md).

## 3. Estável

Com o Validar verde e ao menos uma beta, a versão perde o sufixo, e o PR da
`devel/devel` para a `main` entra com merge commit. O Release da `main`
publica a estável. Depois, a `devel/devel` é alinhada à `main`.
[Guia](https://github.com/IunaMC/modpack/blob/main/docs/guias/publicar-estavel.md).

O servidor pega a estável no próximo reinício
([decisão 0002](../decisoes/0002-servidor-instala-da-main.md)).

## 4. Propagar

A mesma versão vai para o pack da staff e para o `MODPACK` das configs.
[Propagar](propagar.md).

## 5. Configs

O `minecraft-config` publica a própria versão, testada com o pack novo, e
alguém da equipe envia as configs ao servidor.
[Enviar as configs](enviar-configs.md).

## Regras de versão

SemVer no `version` do `pack/pack.toml`, com os critérios de MAJOR, MINOR e
PATCH no
[versionamento do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/versionamento.md).
O `minecraft-config` e o `modpack-moderacao` seguem SemVer próprio, cada um
documentado no seu repositório.
