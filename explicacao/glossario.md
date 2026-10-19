# Glossário

O nome técnico de cada peça do IUNA e onde ela está. Serve para falar do
projeto com quem é de fora (README, currículo, conversa) sem inventar nome.
Como as peças se ligam está na [arquitetura](arquitetura.md).

> O IUNA é um modpack definido como código (*pack-as-code*, packwiz), validado
> por CI com *quality gates*, empacotado em artefatos versionados por SemVer,
> publicado de forma automática no Modrinth e na CurseForge (*release
> automation*) e provisionado no servidor a cada boot.

## De `.zip` à mão para uma esteira

| Antes | Agora | Termo |
| --- | --- | --- |
| `.zip` montado à mão | `pack/` com um `.pw.toml` por mod | *pack-as-code*, fonte única da verdade (*single source of truth*) |
| "Acho que está funcionando" | servidor sobe de verdade no CI com as configs | teste de integração, *smoke test* de boot |
| Número de versão no nome do arquivo | `version` no `pack/pack.toml`, tag e release geradas | SemVer, *release automation* |
| Subir o arquivo em cada site | um push publica nos dois | *multi-platform publishing* |
| Ver se saiu mod novo | issue semanal com o que tem versão nova | *dependency update automation* |
| Atualizar o servidor à mão | instala da `main` a cada boot | *provisioning* declarativo |

## Repositórios e colaboração

| Termo | No IUNA | Onde |
| --- | --- | --- |
| *Multi-repo* (*polyrepo*) | um repositório por papel: pack, moderação, configs, infra, docs, issues, perfil | [Repositórios](../referencia/repositorios.md) |
| *Branching strategy* | `devel/devel` (desenvolvimento, permanente) e `main` (só estáveis) | [versionamento do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/versionamento.md) |
| *Conventional Commits* | `feat(mods): adiciona <Nome> <versão>`, um commit por mod | idem |
| *Signed commits* (GPG + DCO) | `git commit -S -s` | idem |
| *Pull request* com merge commit | a `main` só recebe PR com `--merge` | idem |
| *Changelog* | notas da versão | [`MUDANCAS.md`](https://github.com/IunaMC/modpack/blob/main/MUDANCAS.md) |
| *Architecture Decision Record* (ADR) | decisões numeradas, com contexto e consequências | [`decisoes/`](../decisoes/0001-repos-separados-por-papel.md) |

## Dependências e manifesto

| Termo | No IUNA | Onde |
| --- | --- | --- |
| *Manifest* | descreve o pack: Minecraft, NeoForge, versão | [`pack/pack.toml`](https://github.com/IunaMC/modpack/blob/main/pack/pack.toml) |
| *Dependency* | cada mod, com `side` (`client`, `server`, `both`) | `pack/mods/*.pw.toml` |
| *Lock* de versões e hashes | hash `sha256` de cada arquivo, conferido no CI | `pack/index.toml` e o `[download]` de cada `.pw.toml` |
| *Dependency update automation* | issue semanal com os mods que têm versão nova | workflow *Atualizações de mods* |
| *Version pinning* + Dependabot | packwiz numa versão fixa; actions atualizadas pelo Dependabot | `.github/actions/packwiz`, `.github/dependabot.yml` |
| *External artifact* | jar sem download fixo, guardado numa release própria | [arquivos externos](https://github.com/IunaMC/modpack/blob/main/docs/guias/arquivos-externos.md) |

## CI/CD

| Termo | No IUNA | Onde |
| --- | --- | --- |
| *Workflow* | cada `.yaml` do GitHub Actions | [workflows do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/workflows.md) |
| *Trigger* | push, cron semanal, `workflow_dispatch` | bloco `on:` de cada workflow |
| *Job* e *step* | `validar` → `servidor` (com `needs`), `versao` → `release` | `validar.yaml`, `release.yaml` |
| *Composite action* | instala o packwiz e confere o índice | `.github/actions/packwiz` |
| *Concurrency* | impede duas execuções do mesmo workflow na mesma branch | bloco `concurrency:` |
| *CI* | o Validar | idem |
| *Quality gate* | README em dia, fonte da CurseForge certa, índice sem hash errado, servidor sobe | Validar; o Release recusa versão inválida |
| *Build artifact* | `.mrpack` (Modrinth) e `.zip` (CurseForge) | `packwiz mr export`, `packwiz curseforge export` |
| *CD*, *release automation* | tag, GitHub Release e publicação nas duas plataformas | `release.yaml` |
| *Pre-release* | beta `X.Y.Z-beta.N`, publicada por push na `devel/devel` | [versionamento](https://github.com/IunaMC/modpack/blob/main/docs/referencia/versionamento.md) |
| *Idempotência* | se a release já existe, só republica nas plataformas | job `versao` do Release |
| *Dry run* | `--simular` mostra o que seria enviado | [scripts do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/scripts.md) |
| *Secrets* | tokens como secrets do repositório, nunca no código | [segredos do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/segredos.md) |
| *Scheduled job* | atualizações e resumo toda segunda | *Atualizações de mods*, *Resumo semanal* |

## Qualidade e operação

| Termo | No IUNA | Onde |
| --- | --- | --- |
| *Smoke test* de boot | sobe um servidor real com as configs e espera o "Done" | [servidor local](https://github.com/IunaMC/modpack/blob/main/docs/guias/servidor-local.md) |
| Paridade local/CI | tudo que o CI faz tem comando local | `scripts/op.sh` |
| *Runbook* | passo a passo para o que dá errado | [se o GitHub cair](../processo/se-o-github-cair.md) |
| *Provisioning* | o servidor roda o `packwiz-installer` contra `iuna.space/pack/pack.toml` a cada boot | [decisão 0002](../decisoes/0002-servidor-instala-da-main.md) |
| *Config as code* | `config/` e `server.properties` num repositório próprio, com a versão do pack testada | `minecraft-config` (privado) |
| *Status report* automatizado | issue semanal com o estado dos repositórios | *Resumo semanal* |
| *Rollback* | instalar o `.mrpack` de uma release anterior ou fixar a tag no servidor | GitHub Releases |

## Distribuição

| Termo | No IUNA |
| --- | --- |
| *Distribution channel* | Modrinth e CurseForge |
| *Store listing* como código | textos, links e galeria do Modrinth em `modrinth/`, aplicados pelo workflow |
| *Redistribution compliance* | mods "All Rights Reserved" e o pedido de permissão em `modrinth/permissoes.md` |
| *Redirect*, atalho | `iuna.space/modpack`, `/mrpack` e `/pack/pack.toml` ([arquitetura](arquitetura.md#atalhos-do-domínio)) |

## Termos que parecem iguais e não são

- **Workflow** é o arquivo `.yaml` do GitHub Actions. A sequência de etapas em
  execução é o *pipeline*.
- **Resolução de dependências** é decidir quais versões casam entre si.
  **Provisioning** é o servidor baixar o que o pack manda. O IUNA faz os dois
  em momentos diferentes: ao adicionar o mod e a cada boot.
- **Release** é a versão publicada, **artefato** é o arquivo dela e **tag** é a
  marca no commit.
- **CI** valida cada mudança. **CD** entrega quando a validação passa.
- **Beta** (*pre-release*) sai da `devel/devel`. **Estável** sai da `main`.

## O que ainda não existe

Peças comuns em esteiras desse tipo que o IUNA ainda não tem:

- lint ou testes automatizados dos scripts Python (o CI valida o pack, não o
  código que o valida);
- conferência automática de licença dos mods antes da release (hoje é manual,
  pelo `modrinth/permissoes.md`);
- `CODEOWNERS` e proteção da `main` por *ruleset* (a regra está no `CLAUDE.md`,
  mas o GitHub ainda não a impõe);
- métricas e alertas do servidor em produção documentados.
