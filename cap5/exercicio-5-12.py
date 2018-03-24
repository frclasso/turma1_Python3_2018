#!/usr/bin/env python3

'''Exercício 5.12  Altere o programa anterior de forma a perguntar
também o valor depositado mensalmente. Esse valor será depositado
no início de cada mês, e você deve considerá-lo para o cálculo de
juros do mês seguinte.'''

deposito=float(input('Deposito inicial: '))
taxa=float(input('Taxa de juros: '))
depositoMensal=float(input('Deposito mensal: '))
mes= 1
saldo= deposito
while mes <= 24:
    saldo  = saldo + (saldo * (taxa/100)) + depositoMensal
    print('Saldo do mes %d é de R$%5.2f.' % (mes, saldo))
    #print(f'Saldo do mes {mes} é  de R${saldo:5.2f}')
    mes = mes + 1
print('Ganho total com juros foi de R$%5.2f.' % (saldo - deposito))
#print(f'Ganho total com juros foi de R${saldo - deposito:5.2f}')