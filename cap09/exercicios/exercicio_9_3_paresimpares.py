#!/usr/bin/env python3

# -*- coding:utf-8 -*-

"""​Crie um programa que leia os arquivos pares.txt e “impares.txt” e que
crie um so arquivo “paresimpares” com todas as linhas dos outros dois arquivos,
de forma a preservar a ordem numérica."""


def le_numeros(arquivo):
  while True:
      numero = arquivo.readline()
      if numero =="": return None
      if numero.strip() !="": return int(numero)


def escreve_numero(arquivo, n):
    arquivo.write("%d\n" % n)

pares = open('pares.txt', 'r')
impares = open('impares.txt', 'r')
pares_impares = open('pares_impares.txt', 'w')

npar = le_numeros(pares)
nimpar = le_numeros(impares)

while True:
    if npar == None and nimpar == None:
        break
    if npar != None and (nimpar == None or npar <= nimpar):
        escreve_numero(pares_impares, npar)
        npar = le_numeros(pares)
    if nimpar != None and (npar == None or nimpar<=npar):
        escreve_numero(pares_impares, nimpar)
        nimpar = le_numeros(impares)

pares_impares.close()
pares.close()
impares.close()