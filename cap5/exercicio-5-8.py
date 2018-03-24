'''Exercício 5.8 Escreva um programa que leia dois números.
Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
 Lembre-se de que podemos entender a multiplicação de dois números como
 somas sucessivas de um deles. Assim, 4x5 = 5+5+5+5 =  4+4+4+4+4
'''

p = int(input("Primeiro numero: "))
s = int(input("Segundo numero: "))
x =1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print('%d x %d = %d' % (p, s, r))