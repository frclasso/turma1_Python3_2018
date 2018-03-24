'''Exercício 4.6 Escreva um programa que pergunte a distância que um
passageiro deseja percorrer em km. Calcule o preço da passagem ,
cobrando R$0.50 por km para viagem de até 200km, e R$ 0.45
para viagens mais longas.
'''

distancia =float(input("Digite a distancia a percorrer: "))
if distancia <= 200:
    passagem = 0.50 * distancia
else:
    passagem = 0.45 * distancia
print("Preco da passagem:  R$%7.2f" % passagem)