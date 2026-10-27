# Padrão de escrita

Vale para toda documentação da IunaMC: este repositório, os `docs/` de cada
repositório, os READMEs e os `CONTRIBUTING.md`. As skills do Claude Code e o
`CLAUDE.md` seguem o mesmo padrão de linguagem, mas o formato delas é próprio.

## Onde cada coisa mora

- **Um assunto, um arquivo.** Os outros lugares só linkam. Se a mesma regra
  aparece em dois arquivos, um deles vira link.
- **Muda com o código, fica com o código.** Comandos, scripts, workflows e
  regras de um repositório ficam nos `docs/` dele. O que atravessa
  repositórios fica aqui.
- **Público ou privado.** Repositório público não leva DNS interno, IP,
  hardware, nome da hospedagem, segredo, caminho local nem comando de staff.
  Isso fica no `minecraft-infra` ou no `minecraft-config`, que são privados, e
  a página pública só diz que existe.

## Tipos de página

| Tipo | Responde | Forma |
| --- | --- | --- |
| **Guia** | Como faço X? | Objetivo numa linha, pré-requisitos, passos numerados com os comandos, como verificar e a skill equivalente, se houver |
| **Referência** | O que é X, exatamente? | Tabelas e listas, sem narrativa; espelha o código (workflows, scripts, segredos) |
| **Explicação** | Por que é assim? Como as peças se ligam? | Texto corrido, diagrama quando ajuda |
| **Decisão** | O que decidimos, e por quê? | `Contexto`, `Decisão`, `Consequências`, com data e commit ou PR de origem |

Uma página tem um tipo só. Guia que começa a explicar o porquê linka para a
explicação.

## Decisões

- Nome: `decisoes/NNNN-titulo-curto.md`, numeradas em ordem.
- Cabeçalho: `Data`, `Estado` (`aceita`, `substituída por NNNN`) e `Origem`
  (commit, PR ou issue).
- Não invente motivo. O que não está no repositório, no histórico do git ou
  numa conversa registrada fica como **a confirmar**.
- A decisão não muda depois de aceita. Se mudar, escreva outra e marque a
  antiga como substituída. Assim o histórico mostra o que se sabia e o que se
  decidiu em cada data.
- Esclarecimentos que não mudam a decisão são permitidos: um exemplo, um link,
  um erro de digitação, um nome que mudou. Vão numa seção `## Notas` no fim,
  cada um começando por *Nota de DD/MM/AAAA:*, sem reescrever o texto
  original.

## Texto

- Português do Brasil. Inglês só como tradução à parte (`README.en.md`). A
  exceção é a descrição da CurseForge, só em inglês.
- Frases curtas, voz ativa, segunda pessoa nos guias ("rode", "confira").
- Termo técnico em inglês vai em itálico na primeira vez, se não tiver
  tradução corrente (*pipeline*, *quality gate*). Nome de arquivo, comando,
  branch e variável vão entre crases.
- Datas como `19/10/2026`, versões como `v3.3.0` (tag) ou `3.3.0` (número).

## Issues

- Título no formato `<área>: <o que muda>`, em português e no presente:
  `scripts: op.sh ci espera o Validar e mostra só o erro`. A área é o que o
  Conventional Commit usaria como escopo (`scripts`, `docs`, `infra`, `brand`).
- O corpo diz o que acontece hoje, a proposta e quando está pronto.
- Toda issue de trabalho planejado entra no
  [roadmap](../processo/roadmap.md).

## Formato

- Um `#` por arquivo, que é o título. Seções com `##` e `###`.
- Arquivos e pastas em minúsculas, com hífen e sem acento:
  `publicar-estavel.md`.
- Links relativos dentro do mesmo repositório. Entre repositórios, URL
  completa `https://github.com/IunaMC/<repo>/blob/main/...`.
- Bloco de código com a linguagem (`sh`, `toml`, `yaml`). Um comando por bloco
  quando a pessoa vai copiar.
- A parte mecânica fica com o `markdownlint` (configuração em
  `.markdownlint-cli2.yaml`). O tamanho de linha é livre, e HTML só entra em
  `<details>` e nos comentários que scripts usam como marcador.

## Manutenção

- Mudou skill, workflow ou script? Atualize o guia ou a referência **no mesmo
  commit**.
- Página nova entra no índice do repositório (`SUMMARY.md` aqui, `docs/README.md`
  nos outros).
- Link quebrado e estilo são conferidos no CI. O conteúdo, quem confere é quem
  revisa.
