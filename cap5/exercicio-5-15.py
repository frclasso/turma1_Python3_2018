'''Exercício 5.15  - Escreva um programa para controlar uma pequena máquina
registradora. Você deve solicitar ao usuário que digite o código do produto
 e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o
preço de cada produto.'''


valorAPagar = 0
while True:
    codigo=int(input('Digite codigo da mercadoria: '))
    preco=0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.0
    else:
        print('Codigo invalido')
    if preco != 0:
        quantidade = int(input('Quantidade: '))
        valorAPagar = valorAPagar + (preco * quantidade)
print('Total a pagar: R$%.2f ' % valorAPagar)