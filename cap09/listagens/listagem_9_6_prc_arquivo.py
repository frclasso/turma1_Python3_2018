#!/usr/bin/env python3
# -*-coding:utf-8-*-
largura = 79
entrada = open("entrada.txt")
for linha in entrada.readlines():
     if linha[0] == ";":
         continue
     elif linha[0] == ">":
         print(linha[1:].rjust(largura))
     elif linha[0] == "*":
         print(linha[1:].center(largura))
     else:
         print(linha)
entrada.close()
