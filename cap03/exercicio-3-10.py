"""Exercício 3.10 - Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

salario=float(input("Digite seu salario: "))
porcentagemAumento =float(input("Digite a porcentagem de aumento , "
                                "<<digite apenas numeros>>: "))
aumento = salario * porcentagemAumento/100
novoSalario = salario + aumento

print("Voce teve um aumento de R$%5.2f" % aumento)
print("Seu novo salario é R$%7.2f " % novoSalario)
print("O percentual de aumento foi de %.f%%" % porcentagemAumento)