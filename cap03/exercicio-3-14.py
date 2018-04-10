'''Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos
 por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
 o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
 custa R$60 por dia e R$0.15 por km rodado.
'''

km=int(input("Quantida de quilometros rodados: "))
dias=int(input("Dias de carro alugado: "))
precoPorDia=60
precoPorKM=0.15
precoPagar = km * precoPorKM + dias * precoPorDia
print("Total a pagar: R$%5.2f" % precoPagar)