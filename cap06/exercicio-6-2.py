"""Exercício 6.2  Faça um programa que leia duas listas e que gere uma terceira
 com os elementos das duas primeiras."""

primeiraLista = []
segundaLista = []

while True:
    e = int(input('Digite um valor para primeira lista: '))
    if e ==0:
        break
    primeiraLista.append(e)

while True:
    e = int(input('Digite um valor para segunda lista: '))
    if e ==0:
        break
    segundaLista.append(e)
terceira = primeiraLista[:]
terceira.extend(segundaLista)
x = 0
while x < len(terceira):
    print('{}: {}'.format(x, terceira[x]))
    x+=1

print(id(primeiraLista))
print((id(segundaLista)))
print(id(terceira))