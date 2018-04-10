#!/usr/bin/env python3

'''Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
digitado pelo usuário,mas dessa vez, apenas os números ímpares.
'''

fim = int(input('Digite ultimo numero: '))
x =1
while x <= fim:
    print(x, end='-')
    x =  x + 2