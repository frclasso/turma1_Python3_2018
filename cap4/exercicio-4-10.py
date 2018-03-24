#!/usr/bin/env python3

'''Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
 de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
  R para residências, I para indústrias e C para comércio.
  Calcule o preço a pagar de acordo com a tabela a seguir.
'''

consumo = int(input("Consumo em KWh: "))
tipo = input("Tipo de instalacao (R, C, I): ")
if tipo == 'R' or tipo == 'r':
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C' or tipo == 'c':
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'I' or tipo == 'i':
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print('Erro, tipo de instalacao desconhecido')
custo = consumo * preco
print('Valor a pagar: R$%6.2f' % custo)

