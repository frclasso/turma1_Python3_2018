#!/usr/bin/env python3

# -*-coding:utf-8 -*-

""" Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo."""

import sys

if len(sys.argv)!=2:
    print("\nUso: e09-11.py arquivo1\n\n\n")
    sys.exit(1)

nome=sys.argv[1]
contador = {}

arquivo = open(nome, "r",encoding="utf-8")
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split()
    for p in palavras:
        if p in contador:
            contador[p]+=1
        else:
            contador[p]=1
arquivo.close()

for chave in contador:
    print("{} = {}".format(chave, contador[chave] ))

