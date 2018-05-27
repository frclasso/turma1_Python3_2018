"""Exercício 9.1​ Escreva um programa que receba o nome de um arquivo
pela linha de comando e que imprima todas as linhas desse arquivo."""

import sys

if(len(sys.argv)!=2):
    print('Erro, uso correto: arquivo.py nome_do_arquivo\n\n')
else:
    nome=sys.argv[1]
    arquivo=open(nome, 'r')
    for linha in arquivo.readlines():
        print(linha[:-1])

arquivo.close()

