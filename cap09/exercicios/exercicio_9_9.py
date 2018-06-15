#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""Crie um programa que receba uma lista de nomes de arquivo
 e os imprima,um por um."""

import sys

if len(sys.argv)<2:
    print("\nUso: e09-09.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

for nome in sys.argv[1:]:
    arquivo = open(nome, "r")
    for linha in arquivo:
        print(linha,end="")
    arquivo.close()
