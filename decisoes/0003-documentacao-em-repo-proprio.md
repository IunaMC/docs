# 0003: documentação em repositório próprio

- **Data:** 19/10/2026
- **Estado:** aceita
- **Origem:** criação deste repositório

## Contexto

A documentação cresceu dentro do `modpack`. O manual de operação
(`docs/operacao.md`) descrevia os seis repositórios, o fluxo entre eles, o
envio das configs e a contingência, e o `minecraft-config` linkava para ele.
A mesma regra aparecia no `CLAUDE.md`, no README, no manual e nas skills, e
algumas versões já divergiam. Também se planeja um site de documentação
(MkDocs ou GitBook), com uma parte pública para jogadores e uma wiki interna
da equipe.

## Decisão

- **O que muda junto com o código de um repositório fica nele.** Comandos,
  guias de tarefa, referência de scripts, workflows e segredos.
- **O que atravessa repositórios vem para `IunaMC/docs`.** Arquitetura,
  processo entre repositórios, cargos, glossário e decisões transversais.
- Este repositório é público. O que é interno (host, hardware, comandos de
  staff, nós de permissão) fica no `minecraft-infra` ou no `minecraft-config`.
- Um [padrão de escrita](../referencia/padrao-de-escrita.md) único para todos,
  com links e estilo conferidos no CI.
- A estrutura (`SUMMARY.md`, pastas por tipo de página) já serve de navegação
  para o site futuro.

## Consequências

- Uma mudança de processo pode tocar dois repositórios: o guia no repositório
  do código e a página de processo aqui.
- Os links entre repositórios usam a `main`. Página nova no `modpack` só
  resolve depois da estável seguinte.
- A documentação dos processos automáticos e manuais fica para depois de
  revisá-los ([o que só uma pessoa faz](../processo/manual.md)).

## Notas

- *Nota de 20/10/2026:* exemplos do critério.
  - O guia de adicionar um mod fica no `modpack`: os comandos são do
    `curseforge.py` e do `op.sh` de lá, e mudam com eles.
  - O ciclo de versão fica aqui: passa pelo `modpack`, pela moderação e pelas
    configs, e nenhum deles sozinho o descreve.
  - Os cargos e os comandos do jogador ficam aqui, porque são públicos. Os nós
    de permissão e os comandos da staff ficam no `minecraft-config`, que é
    privado.
  - A regra de versão da `main` fica no `modpack`
    (`docs/referencia/versionamento.md`), porque o `pack.py conferir` de lá a
    aplica. Aqui só há o link.
