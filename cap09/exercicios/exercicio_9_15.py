#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""Altere o programa da listagem 7.5, o jogo da forca.
Utilize um arquivo em que uma palavra seja gravada a cada linha.
Use um editor de textos para gerar o arquivo. Ao iniciar o programa,
utilize esse arquivo para carregar a lista de palavras.
Experimente também perguntar o nome do jogador e gerar um arquivo com
 o número de acertos dos cinco melhores."""

import  sys
import random

palavras = []
placar = {}

def carrega_palavras():
     arquivo = open("palavras.txt","r",encoding="utf-8")
     for palavra in arquivo.readlines():
          palavra = palavra.strip().lower()
          if palavra!="":
               palavras.append(palavra)
     arquivo.close()

def carrega_placar():
     arquivo = open("placar.txt","r",encoding="utf-8")
     for linha in arquivo.readlines():
          linha = linha.strip()
          if linha!="":
               usuario, contador = linha.split(";")
               placar[usuario]=int(contador)
     arquivo.close()

def salva_placar():
     arquivo = open("placar.txt","w",encoding="utf-8")
     for usuario in placar.keys():
          arquivo.write("%s;%d\n" %( usuario, placar[usuario] ))
     arquivo.close()

def atualize_placar(nome):
     if nome in placar:
          placar[nome]+=1
     else:
          placar[nome]=1
     salva_placar()

def exibe_placar():
     placar_ordenado = []
     for usuario, score in placar.items():
          placar_ordenado.append([usuario, score])
     placar_ordenado.sort(key = lambda score: score[1])
     print("\n\nMelhores jogadores por número de acertos:")
     placar_ordenado.reverse()
     for up in placar_ordenado:
          print("%30s %10d" % (up[0],up[1]))


carrega_palavras()
carrega_placar()

palavra = palavras[random.randint(0,len(palavras)-1)]

digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         nome = input("Digite seu nome: ")
         atualize_placar(nome)
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
     print("X==:==\nX  :   ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:
         print("Enforcado!")
         break

exibe_placar()
