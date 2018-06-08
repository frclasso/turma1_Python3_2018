#!/usr/bin/env python3

# -*-coding:utf-8 -*-

"""Crie um programa que imprima as linhas de um arquivo.
Esse programa deve receber três parâmetros pela linha de comando:
o nome do arquivo, a linha inicial e a última linha a imprimir"""

# Idêntico ao exercício 9.02
import sys

# Verifica se os parâmetros foram passados
if(len(sys.argv)!=4): # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-13.py nome_do_arquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome,"r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        print(linha[:-1]) # Como a linha termina com ENTER,
                          # retiramos o último caractere antes de imprimir
    arquivo.close()

# Não esqueça de ler sobre encodings
# Dependendo do tipo de arquivo e de seu sistema operacional,
# ele pode não imprimir corretamente na tela.

