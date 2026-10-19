# Contribuir

## Antes de escrever

- Confira se o assunto é deste repositório: o que muda junto com o código de
  um repositório fica nele, e aqui só entra o que atravessa repositórios
  ([decisão 0003](decisoes/0003-documentacao-em-repo-proprio.md)).
- Siga o [padrão de escrita](referencia/padrao-de-escrita.md).
- Página nova entra também no [`SUMMARY.md`](SUMMARY.md).

## Commits

Os mesmos dos outros repositórios da IunaMC:

- assinados e com DCO: `git commit -S -s`;
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/) em
  português: `docs: …`, `docs(processo): …`, `build(workflows): …`;
- sem `Co-Authored-By` nem menção a ferramentas de IA.

## Checagem

O workflow [Validar](.github/workflows/validar.yaml) roda em todo push e PR:
links internos e âncoras (`lychee --offline`) e estilo (`markdownlint-cli2`,
regras em [`.markdownlint-cli2.yaml`](.markdownlint-cli2.yaml)). Para rodar na
sua máquina:

```sh
npx markdownlint-cli2 '**/*.md'
```

```sh
docker run --rm -v "$PWD:/docs" -w /docs lycheeverse/lychee --offline --include-fragments '**/*.md'
```
