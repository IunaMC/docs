# Processos manuais

O que não tem automação, por que continua assim e o que já ajuda. A lista
foi revisada em 20/10/2026. O que roda sozinho está em
[processos automáticos](automatico.md).

## Só uma pessoa faz

| Processo | Por que é manual | O que ajuda |
| --- | --- | --- |
| Enviar as configs ao servidor e reiniciar pelo painel ([processo](enviar-configs.md)) | Decisão: os segredos não saem do GitHub dentro do `.zip`, e o envio troca a `config/` inteira, com risco para o `world/` se for feito às cegas | A release testa o servidor antes; a issue **Enviar configs X.Y.Z** guarda o checklist; o Resumo semanal lista os envios pendentes; a comparação com a cópia do servidor vai virar script ([minecraft-config#10](https://github.com/IunaMC/minecraft-config/issues/10)) |
| Colar a descrição e trocar as imagens do projeto na CurseForge; acompanhar a revisão dos arquivos | A CurseForge não tem API para isso. A de upload só envia arquivos, a de leitura só mostra os aprovados, e o painel de autor só aceita a sessão do navegador (estudado em 19/10/2026) | `curseforge.py descricao` gera o texto, `curseforge.py status` diz o que já aparece, e o Resumo semanal avisa quando falta colar |
| Pedidos de permissão no Modrinth e a moderação de lá | É conversa com os autores dos mods | O registro fica no `modrinth/permissoes.md` do `modpack` |
| Criar e editar regras do domínio no painel da Cloudflare ([atalhos](../explicacao/arquitetura.md#atalhos-do-domínio)) | Mudam raramente | Backup semanal e a migração entre domínios já são workflows ([migrar o domínio](migrar-dominio.md)) |
| Cargos: LuckPerms pelo console e sincronia com o Discord ([cargos](../servidor/cargos.md)) | Quem ganha cargo é decisão sobre pessoas | Os grupos e as regras estão no `minecraft-config` |
| Gerar e renovar os tokens dos workflows ([segredos do modpack](https://github.com/IunaMC/modpack/blob/main/docs/referencia/segredos.md)) | O valor não pode passar pelo repositório nem pelo Claude | Token vencido aparece no Validar ou no Resumo; o aviso de vencimento antecipado vai virar script ([modpack#23](https://github.com/IunaMC/modpack/issues/23)) |
| Confirmar uma versão MAJOR | MAJOR pede mundo novo ou reinstalar tudo | A Entrada na main recusa o PR sem "MAJOR confirmado" no corpo |

## Ainda pela skill, vai virar script

Estes passos são mecânicos, mas hoje dependem de uma skill do Claude Code.
Sem ela, são feitos à mão pelos guias de cada repositório. Cada um tem uma
issue com o passo atual e o script proposto.

| Skill | Passo | Issue |
| --- | --- | --- |
| `/add-mod` (modpack) | Definir o lado de cada mod pelo Modrinth | [modpack#17](https://github.com/IunaMC/modpack/issues/17) |
| `/remover-mod` | Achar dependências órfãs e configs que sobram | [modpack#18](https://github.com/IunaMC/modpack/issues/18) |
| `/beta` | Versão, `refresh`, README, commit, push e acompanhar o Release | [modpack#19](https://github.com/IunaMC/modpack/issues/19) |
| `/estavel` | PR, merge, Release e alinhar a `devel/devel` | [modpack#20](https://github.com/IunaMC/modpack/issues/20) |
| `/propagar` | Moderação (refazer o commit do bot com assinatura, PR, merge) e `MODPACK` | [modpack#21](https://github.com/IunaMC/modpack/issues/21) |
| `/testar` (modpack) | Esperar o Validar e mostrar só o erro | [modpack#22](https://github.com/IunaMC/modpack/issues/22) |
| `/enviar-configs` | Comparar a `config/` do servidor com o repositório | [minecraft-config#10](https://github.com/IunaMC/minecraft-config/issues/10) |
| `/versao` e `/testar` (configs) | Versão, conferência dos marcadores e teste | [minecraft-config#11](https://github.com/IunaMC/minecraft-config/issues/11) |
| `/add-mod` (moderação) | Achar o que o pack base já tem | [modpack-moderacao#8](https://github.com/IunaMC/modpack-moderacao/issues/8) |

Continuam com pessoa ou com a skill: escrever o `MUDANCAS.md` e o texto dos
PRs, achar o Project ID da CurseForge de um mod novo e ler perfis do Spark.

O commit do bot da moderação vem sem assinatura porque o GitHub Actions não
tem a chave de quem mantém o projeto. Por isso ele é refeito antes do PR.
