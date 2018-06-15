#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""Crie um programa que receba uma lista de nomes de arquivos e que gere
 apenas um grande arquivo de saída."""

import sys

if len(sys.argv)<2:
    print("\nUso: e09-10.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

saida = open("saida_unica.txt","w", encoding="utf-8")
for nome in sys.argv[1:]:
    arquivo = open(nome, "r",encoding="utf-8")
    for linha in arquivo:
        saida.write(linha)
    arquivo.close()
saida.close()
