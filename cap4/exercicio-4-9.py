#!/usr/bin/env python3

'''Escreva um programa para aprovar o empréstimo bancário para comprar de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos
 a pagar. O valor da prestação mensal, não pode ser superior a 30% do salário.
 Calcule o valor da prestação  como sendo o valor da casa a comprar dividido pelo
 número de meses a pagar.
'''

valor=float(input("Digite valor da casa: "))
salario=float(input("Digite salario: "))
qtdAnos=int(input("Anos do financiamento: "))
meses = qtdAnos * 12
prestacao= valor / meses
if prestacao > salario * 0.3:
    print('Emprestimo negado')
else:
    print('Emprestimo Aprovado, valor da prestacao R$%6.2f ' % prestacao)
    #print(f'Emprestimo Aprovado, valor da prestacao R${prestacao:6.2f} ')