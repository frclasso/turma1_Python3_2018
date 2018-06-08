#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""​Modifique o programa anterior para também registrar a linha e a coluna
de cada ocorrência da palavra no arquivo. Para isso, utilize listas nos
valores de cada palavra, guardando a linha e a coluna de cada ocorrência."""

import sys

if len(sys.argv)!=2:
    print("\nUso: e09-12.py arquivo1\n\n\n")
    sys.exit(1)

nome=sys.argv[1]
contador = {}
clinha = 1
coluna = 1

arquivo = open(nome, "r",encoding="utf-8")
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split(" ") # Com parâmetro considera os espaços repetidos
    for p in palavras:
        if p == "":
            coluna +=1
            continue
        if p in contador:
            contador[p].append((clinha, coluna))
        else:
            contador[p]=[ (clinha, coluna) ]
        coluna += len(p)+1
    clinha+=1
    coluna=1
arquivo.close()

for chave in contador:
    print("{} = {}".format(chave, contador[chave] ))

