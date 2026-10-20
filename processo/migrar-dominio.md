# Migrar o domínio

Objetivo: trocar o domínio do projeto (por exemplo, de `exemplo.com` para
`exemplo.net`) sem quebrar os links em uso nem o e-mail.

O passo a passo, o script e o workflow ficam no `minecraft-infra`, que é
privado e guarda o token da Cloudflare. Esta página só dá a ordem.

1. Crie a zona nova na Cloudflare, na mesma conta da antiga.
2. No `minecraft-infra`, simule a cópia de regras, DNS, ajustes e Email Routing
   e depois aplique (workflow *Cloudflare* ou `scripts/cloudflare.py`).
3. Confira o destino com a ação `verificar`.
4. Gere de novo o DKIM do provedor de envio e confira o DMARC e o BIMI.
5. Teste os redirects e um e-mail de verdade.
6. Troque os links dos repositórios, um commit por repositório. O servidor em
   produção instala o pack por um desses links, então troque o `compose/` só
   depois do teste do passo 5.
7. Mantenha o domínio antigo redirecionando até o comando `uso` mostrar zero
   acessos. O comando `links` lista o que ainda aponta para ele.

Ver também: [Repositórios](../referencia/repositorios.md).
