"""Exercício 6.8​ Modifique o primeiro exemplo (Listagem 6.23) de
 forma a realizar a mesma tarefa, mas sem utilizar a variável ‘achou’.
  Dica: observe a condição de saída do ​while​."""


L = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
x = 0
while x < len(L):
    if L[x] == p:
        print(f'{p} achado posicao {x}')
        break
    x+=1
else:
    print(f'{p} nao encontrado.')