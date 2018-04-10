#!/usr/bin/env/ python3

L = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x+=1
# if achou:
#     print(f'{p} achado na posicao {x}')
# else:
#     print(f'{p} nao encontrado.')

#print('{} achado na posicao {} '.format(p, x)) if achou else print('{} nao encontrado.'.format(p))

print(f'{p} achado na posicao {x} ') if achou else print(f'{p} nao encontrado.')

