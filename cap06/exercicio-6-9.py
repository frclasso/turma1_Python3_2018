"""
Exercício 6.9 ​Modifique o exemplo para pesquisar dois valores.
Em vez de apenas ‘p’, leia outro valor ‘v’ que também será procurado.
Na impressão, indique qual dos dois valores foi achado primeiro.
"""

L = [15,7,27,39]
p = int(input('Digite o valor a procurar(p): '))
v = int(input('Digite o valor a procurar (v): '))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2

    x += 1

print(f'{p} encontrado') if achouP else print(f'{p} nao encontrado')

print(f'{v} encontrado.')if achouV else print(f'{v} nao encontrado.')

if primeiro == 1:
    print('p foi econtrado antes de v')
if primeiro == 2:
    print('v foi encontrado antes de p')