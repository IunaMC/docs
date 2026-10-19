# Se o GitHub cair

O servidor roda o `packwiz-installer-bootstrap` a cada boot, contra
`https://iuna.space/pack/pack.toml`. O atalho só redireciona para o GitHub,
então, sem acesso ao GitHub, o instalador falha. Os jars da última instalação
continuam na pasta `mods/`.

1. Se a falha impedir a subida, tire temporariamente o instalador do comando de
   inicialização no painel. O servidor sobe com o que já tem.
2. Quando o GitHub voltar, devolva o instalador ao comando e reinicie.

Para reinstalar do zero sem GitHub, use o `.mrpack` da última release guardado
fora do GitHub.
