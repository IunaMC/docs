# Processos automáticos

O que roda sozinho na IunaMC, em todos os repositórios: quando roda, o que
faz e onde ver o resultado. O detalhe de cada workflow (entradas, segredos,
equivalente local) fica na referência do repositório dono, linkada no fim. O
que continua com uma pessoa está em [processos manuais](manual.md).

## Por horário

Os workflows de agenda só rodam na `main` do repositório.

| Quando | Repositório | Workflow | Resultado |
| --- | --- | --- | --- |
| Todo dia, 09h17 UTC (06h17 em Brasília) | `modpack-moderacao` | Acompanhar pack base | Se o `modpack` tem estável nova, a branch `base/vX.Y.Z` e o PR (ou uma issue, se o Actions não puder abrir PR) |
| Segunda, 06h17 UTC (03h17) | `minecraft-infra` | Cloudflare backup | Artefato com a configuração das zonas do domínio |
| Segunda, 10h23 UTC (07h23) | `modpack` | Atualizações de mods | Issue fixa **Mods com versão nova**, fechada quando não há nada pendente |
| Segunda, 10h53 UTC (07h53) | `modpack` | Resumo semanal | Issue fixa **Resumo semanal**: versões dos três repositórios e se estão alinhadas, CI quebrado, commits fora da `main`, PRs e issues abertos, envios de config pendentes, o estado da CurseForge e quando vencem os tokens |

## Por evento

| Repositório | Workflow | Dispara em | Faz | Onde ver |
| --- | --- | --- | --- | --- |
| `modpack` | Validar | Push fora da `main` que mexe no pack, nos scripts, no README ou no CI | Confere o README e a fonte da CurseForge, exporta `.mrpack` e `.zip` de teste e sobe um servidor de verdade com as configs | Aba Actions e o PR da branch; logs do servidor como artefato |
| `modpack` | Entrada na main | PR para a `main` | Confere versão e origem do PR; o ruleset da `main` exige que passe | Checks do PR |
| `modpack` | Release | Push na `main` ou na `devel/devel` com versão nova | Tag, GitHub Release com o `.mrpack`, envio ao Modrinth e à CurseForge. Beta só sai da `devel/devel`, estável só da `main` | Releases, Modrinth, CurseForge (depois da revisão de lá) |
| `modpack` | Modrinth | Push que muda `modrinth/` | Fora da `main`, mostra o que mudaria; na `main`, aplica a página | Log da execução, página do Modrinth |
| `modpack`, `docs` | Docs / Validar | Push ou PR que muda `.md` | Links internos e estilo | Aba Actions |
| `modpack-moderacao` | Validar | Push fora da `main` | Monta o pack sobre o pack base e gera o `.mrpack` de teste | Aba Actions |
| `modpack-moderacao` | Release | Push na `main` com versão nova | Release com o `.mrpack` da moderação | Releases |
| `minecraft-config` | Release | Push na `main` com versão nova; manual em qualquer branch, sem publicar | Sobe um servidor de teste com as configs e o pack do arquivo `MODPACK`; se ele ficar pronto, tag, release com o `.zip` e a issue **Enviar configs X.Y.Z ao servidor** | Releases e a issue com etiqueta `envio` |
| `minecraft-infra` | Cloudflare consultar / migrar | Só manual | Consulta e simula; o migrar grava regras, DNS e e-mail de um domínio em outro | Log da execução |

## Uma estável, de ponta a ponta

```
PR devel/devel → main (modpack)
  ├─ Entrada na main confere a versão
  └─ merge ─► Release: tag, .mrpack, Modrinth, CurseForge
                │
                ├─ servidor instala a main no próximo boot
                ├─ Acompanhar pack base (moderação) ─► PR base/vX.Y.Z ─► Release da moderação
                └─ MODPACK no minecraft-config ─► Release das configs ─► issue de envio
                                                                          │
                                                       envio manual ao servidor (pessoa)
```

Os passos entre o Release do `modpack` e o `MODPACK` são feitos por uma pessoa
com o `op.sh propagar` (ou a skill `/propagar`): veja [propagar uma estável](propagar.md).

## Referência de cada repositório

- `modpack`: [workflows](https://github.com/IunaMC/modpack/blob/main/docs/referencia/workflows.md) e [segredos](https://github.com/IunaMC/modpack/blob/main/docs/referencia/segredos.md).
- `modpack-moderacao`: [`.github/workflows/`](https://github.com/IunaMC/modpack-moderacao/tree/main/.github/workflows) (privado).
- `minecraft-config`: [versões](https://github.com/IunaMC/minecraft-config/blob/main/docs/versoes.md) e [segredos](https://github.com/IunaMC/minecraft-config/blob/main/docs/segredos.md) (privado).
- `minecraft-infra`: [migrar o domínio](migrar-dominio.md) e o guia do repositório (privado).
