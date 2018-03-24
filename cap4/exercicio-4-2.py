'''Exercício 4.2  - Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h , exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa ,
cobrando R$5 por km acima de 80km/h.
'''

velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Voce foi multado em R$%.2f" % multa)
if velocidade <= 80:
    print("Sem multas")