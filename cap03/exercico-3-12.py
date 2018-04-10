'''Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.'''

distancia= float(input("Digite a distancia em km: "))
velocidadeMedia= float(input("Digite a velocidade em km/h: "))
tempo = distancia / velocidadeMedia
print("O tempo estimado para viagem é de %.f horas" % tempo)

#calculando em horas, minutos e segundos

tempos_s = int(tempo * 3600) #CONVERTENDO HORAS PARA SEGUNDOS
horas = int(tempos_s /3600) # SEPARANDO A PARTE INTEIRA
tempos_s = int(tempos_s % 3600) #SEPARANDO O RESTO
minutos = int(tempos_s / 60)
segundos = int(tempos_s % 60)

print("Tempo total %d:%d:%02d" % (horas, minutos, segundos))