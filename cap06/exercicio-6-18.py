'''Exercício 6.18​ Escreva um programa que gere um dicionário, onde
 cada chave seja um caractere, e seu valor seja o número desse caractere
encontrado em uma frase lida.'''

frase = input('Frase: ')
d = {}
for letra in frase:
    if letra == ' ':continue
    if letra in d:
        d[letra] = d[letra] + 1
    else:d[letra] = 1
print(d)

#ou

contadorDeLetras = {}
for letra in frase:
    if letra == ' ':continue
    contadorDeLetras[letra] = contadorDeLetras.get(letra,  0 ) + 1
print(contadorDeLetras)
