#!/usr/bin/env python3
"""Mantém o bloco de regras comuns no CLAUDE.md de cada repositório.

Uso:
  regras-comuns.py [--fonte ARQUIVO] sincronizar REPO...
  regras-comuns.py [--fonte ARQUIVO] conferir [REPO...]

O texto oficial é o trecho entre os marcadores de `referencia/claude.md`.
`conferir` sem caminho confere o diretório atual.
"""
import argparse
import re
import sys
from pathlib import Path

INICIO = "<!-- regras-comuns:inicio -->"
FIM = "<!-- regras-comuns:fim -->"
FONTE = Path(__file__).resolve().parent.parent / "referencia" / "claude.md"


def bloco(texto, origem):
    """Devolve o bloco com os marcadores, ou None se faltar algum."""
    m = re.search(rf"^{re.escape(INICIO)}$.*?^{re.escape(FIM)}$", texto, re.M | re.S)
    return m.group(0) if m else None


def ler_fonte(caminho):
    oficial = bloco(caminho.read_text(encoding="utf-8"), caminho)
    if oficial is None:
        sys.exit(f"erro: marcadores não encontrados em {caminho}")
    return oficial


def sincronizar(oficial, repos):
    for repo in repos:
        arquivo = Path(repo) / "CLAUDE.md"
        if not arquivo.exists():
            sys.exit(f"erro: {arquivo} não existe")
        texto = arquivo.read_text(encoding="utf-8")
        atual = bloco(texto, arquivo)
        if atual is None:
            novo = texto.rstrip("\n") + "\n\n" + oficial + "\n"
            acao = "criado"
        else:
            novo = texto.replace(atual, oficial, 1)
            acao = "igual" if novo == texto else "atualizado"
        if novo != texto:
            arquivo.write_text(novo, encoding="utf-8")
        print(f"{arquivo}: {acao}")


def conferir(oficial, repos):
    divergentes = 0
    for repo in repos:
        arquivo = Path(repo) / "CLAUDE.md"
        atual = bloco(arquivo.read_text(encoding="utf-8"), arquivo) if arquivo.exists() else None
        if atual != oficial:
            divergentes += 1
            motivo = "sem o bloco" if atual is None else "bloco diverge do oficial"
            print(f"{arquivo}: {motivo}", file=sys.stderr)
        else:
            print(f"{arquivo}: ok")
    if divergentes:
        print("Rode `scripts/regras-comuns.py sincronizar <repo>` no IunaMC/docs.", file=sys.stderr)
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fonte", type=Path, default=FONTE, help="texto oficial (padrão: referencia/claude.md)")
    sub = p.add_subparsers(dest="comando", required=True)
    sub.add_parser("sincronizar").add_argument("repos", nargs="+")
    sub.add_parser("conferir").add_argument("repos", nargs="*", default=["."])
    a = p.parse_args()
    oficial = ler_fonte(a.fonte)
    (sincronizar if a.comando == "sincronizar" else conferir)(oficial, a.repos)


if __name__ == "__main__":
    main()
