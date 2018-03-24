'''Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida
de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada
 cigarro, calcule quantos dias de vida um fumante perdera.
 Exiba o total em dias.'''

cigarroPorDia =int(input("Qunatidade de cigarros por dia: "))
anosFumando=float(input("Quantidade de anos fumando: "))
reducaoMinutos = anosFumando * 365 * cigarroPorDia * 10


#UM DIA TEM 24 X 60 MINUTOS
reducaoEmDias = reducaoMinutos / (24 * 60)
print("Reducao em tempo de vida de %.f dias" % reducaoEmDias )