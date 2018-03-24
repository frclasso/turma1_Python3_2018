'''Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+),
subtração (-), multiplicação(*) e divisão(/).
 Exiba o resultado da operação solicitada.'''

a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))

operacaoMatematica = input("Digite a operacao desejada (+.-,/,*): ")
if operacaoMatematica == "+":
    resultado = a + b
elif operacaoMatematica == "-":
    resultado = a - b
elif operacaoMatematica == "/":
    resultado = a /b
elif operacaoMatematica == "*":
    resultado = a * b
else:
    print("Operacao invalida")
print("Resultado da operacao matematica: ", resultado)