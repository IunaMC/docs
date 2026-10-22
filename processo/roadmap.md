# Roadmap

O trabalho planejado da IUNA fica no projeto
[IUNA · Roadmap](https://github.com/orgs/IunaMC/projects/1). As issues vivem
nos repositórios; o projeto só as reúne.

## Campos

| Campo | Valores |
| --- | --- |
| Status | A fazer · Em andamento · Concluído |
| Prioridade | Alta · Normal · Baixa |

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

Criadas na tela do projeto, porque a API não cria visões:

1. **Próximos:** *Board*, colunas por Status, filtro `-status:Concluído`.
2. **Por repositório:** *Table*, *Group by* Repository, *Sort by* Prioridade.
3. **Alta prioridade:** *Table*, filtro `prioridade:Alta -status:Concluído`.

## Automações

Ligadas em *Workflows*, também só pela tela:

- *Item added to project* → A fazer.
- *Item closed* e *Pull request merged* → Concluído.
- *Item reopened* → A fazer.
- *Auto-archive items*: itens concluídos há mais de 14 dias.
- *Auto-add to project*: um filtro só no plano gratuito. Os demais itens
  entram pelo comando acima.
