#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""Modifique o programa da Listagem 9.6 para imprimir 40 vezes o símbolo
de “=” se este for o primeiro caractere da linha. Adicione também a opção
 para parar de imprimir até que se pressione a tecla <ENTER> casa vez que
  a linha iniciar com “.” como primeiro caractere."""


largura=79
entrada=open("entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(largura))
    elif linha[0]=="*":
        print(linha[1:].center(largura))
    elif linha[0]=="=":
        print("=" * 40)
    elif linha[0]==".":
        input("Digite algo para continuar")
        print()
    else:
        print(linha)
entrada.close()
