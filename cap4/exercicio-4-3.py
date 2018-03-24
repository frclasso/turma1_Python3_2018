'''Exercício 4.3 - Escreva um programa que leia três números e que imprima o
 maior e o menor.
'''

a=int(input("Digite primeiro numero:"))
b=int(input("Digite segundo numero: "))
c=int(input("Digite terceiro numero: "))
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print("Maior: %d" % maior)
print("Menor: %d " % menor)