'''Exercício 8.5 ​Reescreva a função da listagem 8.5 de forma a utilizar os
 métodos de pesquisa em listas, vistos no capítulo 7.


Listagem 8.5 - Pesquisa em uma lista

def​ pesquise(lista, valor):
    ​for​ x,e ​in enumerate​(lista):
        ​if​ e == valor: ​return​ x
    ​return​ None ​(2)

L = [10, 20, 25, 30]
print​(pesquise(L, 25))
print​(pesquise(L, 27))
 '''


def pesquisa(lista, valor):
    if valor in lista:
        return lista.index(valor)  # retorna  a posicao/indice
    return None

L = [10, 20, 25, 30]
print(pesquisa(L, 25))
print(pesquisa(L, 27))