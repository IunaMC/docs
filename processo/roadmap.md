# Roadmap

O trabalho planejado da IUNA fica no projeto
[IUNA · Roadmap](https://github.com/orgs/IunaMC/projects/1). As issues vivem
nos repositórios; o projeto só as reúne.

## Campos

| Campo | Valores |
| --- | --- |
| Status | Descartado · Backlog · Pronto · Em andamento · Concluído |
| Prioridade | Longo Prazo · Baixa · Média · Alta · Crítica |

Repositório, tipo (Bug, Feature, Task) e responsável vêm da própria issue.
Não há iteração nem prazo: a ordem vem da prioridade.

## Abrir um item

1. Abra a issue no repositório dono, com título `<área>: <o que muda>` e o
   "pronto quando" no corpo. Defina o tipo da issue.
2. Adicione ao projeto:

   ```sh
   gh project item-add 1 --owner IunaMC --url https://github.com/IunaMC/<repo>/issues/<n>
   ```

3. Ideia sem repositório entra como rascunho e vira issue quando for decidida.

Issue automática (como "Mods com versão nova") não entra.

## Visões

1. **Backlog:** tabela com todos os itens.
2. **Prioridade:** quadro por Status, filtro
   `-is:closed -status:Pronto -status:Descartado`.

A API não cria visões; elas se editam na tela do projeto.

## Automações

Ligadas: item adicionado, item reaberto, PR vinculado, PR mergeado, mudanças
pedidas, revisão aprovada, auto-close da issue e sub-issues. *Item closed*
está desligado.
