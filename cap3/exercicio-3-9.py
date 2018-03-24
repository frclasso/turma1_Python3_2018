'''Exercício 3.9 Escreva um programa que leia a quantidade
 de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.'''

#Um minuto = 60 segundos
#Uma hora = 3600 segundos
#Um dia te 24 horas , logo 24 * 3600 segundos

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos=int(input("Minutos: "))
segundos = int(input("Segundos: "))
totalEmSegundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print("Total convertido em segundos %d segundos." % totalEmSegundos)