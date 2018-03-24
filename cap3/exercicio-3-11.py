'''Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria
 e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.'''

preco=float(input("Digite o preçø da mercadoria: "))
desconto = float(input("Digite valor de desconto, apenas numeros: "))
valorDesconto = preco * desconto/100 #aqui vai ser calculado o percentual de desconto
precoPagar = preco - valorDesconto
print("")
print("O desconto foi de R$%.2f " % valorDesconto)
print("O valor a pagar é de %.f %%" % precoPagar)