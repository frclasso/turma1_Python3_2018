#!/usr/bin/ env python3

'''Exercício 5.11  Escreva um programa que pergunte o depósito inicial e a
taxa de juros de uma poupança. Exiba os valores mês a mês para os
24 primeiros meses.Escreva o total ganho com juros no período.'''

deposito=float(input('Deposito inicial: '))
taxa=float(input('Taxa de juros: '))
mes= 1
saldo= deposito
while mes <= 24:
    saldo  = saldo + (saldo * (taxa/100))
    print('Saldo do mes %d é de R$%5.2f.' % (mes, saldo))
    #print(f'Saldo do mes {mes} é  de R${saldo:5.2f}')
    mes = mes + 1
print('Ganho total com juros foi de R$%5.2f.' % (saldo - deposito))
#print(f'Ganho total com juros foi de R${saldo - deposito:5.2f}')
