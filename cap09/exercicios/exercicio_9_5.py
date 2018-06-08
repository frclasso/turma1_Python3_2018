#!/usr/bin/env python3

# -*-coding:utf-8-*-

pares = open("pares.txt","r")
saida = open("pares_invertido.txt","w")

L = pares.readlines()
L.reverse()
for l in L:
    saida.write(l)

pares.close()
saida.close()