'''Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e
 calcule o valor do aumento. Para salários superiores a R$1.250,00,
 calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''

salario =float(input("Digite salario: "))
#percentualAumento = 0.15
if salario > 1250:
    percentualAumento = 0.10
if salario < 1250:
    percentualAumento = 0.15

aumento = salario * percentualAumento
print("Se aumento sera de  R$%7.2f" % aumento)
