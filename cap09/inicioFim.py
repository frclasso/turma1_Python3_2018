#-*-coding:utf-8 -*-
"""Exercício 9.2 - ​Modifique o programa do exercício 9.1 para que receba
mais dois parâmetros: a linha de início e a de fim para impressão.
O programa deve imprimir apenas as linhas entre esses dois valores(incluindo as
 linhas de início e fim)."""


import sys

if(len(sys.argv)!=4): # aumentamos de 2 para 4
    print('Erro, uso correto: arquivo.py nome_do_arquivo\n\n')
else:
    nome=sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo=open(nome, 'r')
    for linha in arquivo.readlines()[inicio-1: fim]:
        print(linha[:-1])

arquivo.close()
