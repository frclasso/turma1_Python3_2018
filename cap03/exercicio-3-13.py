'''Exercício 3.13 - Escreva um programa que converta uma temperatura digitada
em Celsius em Fahrenheit. A fórmula para essa conversão é:

F = (9 x C /5) + 32
'''

C = float(input("Digite a temperatura em Celsius: "))
F = (9 * C / 5) + 32
print("A temperatura em %.f Celsius equivale a %.f Fahrenheit" % (C,F))