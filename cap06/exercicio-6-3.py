"""Exercício 6.3  Faça um programa que percorra duas listas e gere um terceira
sem elementos repetidos."""

primeiraLista = [1,2,3,4,5,6]
segundaLista = [4,5,6,7,8,3]
# while True:
#     e = int(input('Digite os valores da primeira lista: '))
#     if e == 0:
#         break
#     primeiraLista.append(e)
#
# while True:
#     e = int(input('Digite os valores da segunda lista: '))
#     if e == 0:
#         break
#     segundaLista.append(e)

terceiraLista = []

duas_listas = primeiraLista[:]
duas_listas.extend(segundaLista)

x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceiraLista):
        if duas_listas[x] == terceiraLista[y]:
            break
        y+=1
    if y == len(terceiraLista):
        terceiraLista.append(duas_listas[x])
    x+=1
x=0
while x < len(terceiraLista):
    print('{}: {}'.format(x, terceiraLista[x]))
    x+=1