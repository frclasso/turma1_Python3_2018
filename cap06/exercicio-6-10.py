"""Exercício 6.10 ​Modifique o programa do exercício 6.9 de forma
a pesquisar ‘p’ e ‘v’ em toda a lista e informando o usuário a
posição onde ‘p’ e a posição ‘v’ foram encontrados."""

L = [15,7,27,39]
p = int(input('Digite o valor a procurar(p): '))
v = int(input('Digite o valor a procurar (v): '))
x = 0
achouP = -1  # indica que nao encontramos o valor procurado
achouV = -1

while x < len(L):
    if L[x] == p:
        achouP = x
    if L[x] == v:
        achouV =x
    x+=1

if achouP != -1:
    print(f'p: {p} encontrado na posicao {achouP}')
else:print(f'p: {p} nao encontrado')

if achouV != -1:
    print(f'v: {v} encontrado na posicao {achouV}')
else:print(f'v: {v} nao encontrado.')

if achouP != -1 and achouV!= -1:    # Verifica se ambos foram encontrados
    if achouP <= achouV:
        print('p foi achado antes de v')
    else:
        print('v foi achado antes de p')