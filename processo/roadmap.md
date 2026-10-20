# Roadmap

O trabalho planejado da IUNA fica no projeto
[IUNA · Roadmap](https://github.com/orgs/IunaMC/projects/1) do GitHub: um
lugar só para engenharia, servidor e comunidade, separado pelo campo
Componente. As issues continuam nos repositórios. O projeto só as reúne e diz
em que pé cada uma está.

Os projetos da org seguem o nome `IUNA · <escopo>`. Hoje há um só. Um projeto
novo só aparece quando um escopo precisar de fluxo próprio.

## Campos

### Status

| Valor | Quando |
| --- | --- |
| Backlog | Registrado, ainda sem decisão de fazer |
| Pronto | Decidido e com o "pronto quando" claro; pode ser puxado |
| Em andamento | Alguém está fazendo (branch aberta) |
| Em revisão | PR aberto esperando checks ou leitura |
| Concluído | Issue fechada ou PR mergeado |

### Componente

| Valor | Cobre | Repositório típico |
| --- | --- | --- |
| Pack | mods, versões, `pack/` | `modpack` |
| Configs | `config/`, `server.properties`, segredos marcados | `minecraft-config` |
| Moderação | pack da staff | `modpack-moderacao` |
| Infra | servidor, compose, Pterodactyl, Cloudflare, domínio | `minecraft-infra` |
| CI/CD | workflows, release, trava da `main` | qualquer |
| Docs | documentação, padrão de escrita | `docs` e o `docs/` de cada repositório |
| Brand | logo, BIMI, assets | `brand` |
| Servidor | gameplay, balanceamento, cargos, desempenho | `minecraft-config`, `issues` |
| Comunidade | bugs e sugestões dos jogadores | `issues` |

### Tipo

| Valor | Exemplo |
| --- | --- |
| Feature | algo novo para o jogador ou para a equipe |
| Bug | algo quebrado |
| Automação | passo manual ou de IA que vira script (etiqueta `processo`) |
| Docs | só documentação |
| Manutenção | atualização, limpeza, dívida técnica |

### Prioridade

| Valor | Significa |
| --- | --- |
| P0 · Urgente | quebra a produção ou os jogadores agora; larga o resto |
| P1 · Alta | próximo a ser feito |
| P2 · Normal | entra quando couber (padrão) |
| P3 · Baixa | quando sobrar tempo |

Não há iteração nem prazo: a ordem vem da prioridade.

## Abrir um item

1. Abra a issue no repositório onde a mudança vai morar, com o título
   `<área>: <o que muda>` (por exemplo, `scripts: op.sh ci espera o Validar`) e
   o "pronto quando" no corpo.
2. Adicione ao projeto e preencha Componente, Tipo e Prioridade:

   ```sh
   gh project item-add 1 --owner IunaMC --url https://github.com/IunaMC/<repo>/issues/<n>
   ```

3. Ideia ainda sem repositório definido entra como rascunho, direto no projeto,
   e vira issue quando for decidida.

Issue com a etiqueta `processo` entra sozinha no projeto (abaixo). Fechar a
issue ou mergear o PR leva o item a Concluído.

## Visões e automações

A API do GitHub não cria visões nem liga as automações do projeto, então elas
são feitas na tela do projeto (`...` → *Settings* e *Workflows*).

Visões:

1. **Quadro:** *Board*, colunas por Status, filtro `-status:Concluído`.
2. **Por componente:** *Table*, *Group by* Componente, *Sort by* Prioridade.
3. **Automação:** *Table*, filtro `tipo:Automação`.

Automações (*Workflows*):

- *Item added to project* → Status `Backlog`.
- *Item closed* e *Pull request merged* → Status `Concluído`.
- *Item reopened* → Status `Backlog`.
- *Auto-add to project*: repositório `modpack`, filtro
  `is:issue label:processo`. No plano gratuito, o projeto tem um filtro de
  auto-add só. As issues `processo` do `minecraft-config` e do
  `modpack-moderacao` entram com o `gh project item-add` acima.
