'''Exercício 5.7 Modifique o programa anterior de forma que o usuário
também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
'''

n = int(input("Tabuada de: "))
inicio = int(input('De: '))
fim = int(input("Ate: "))

x =inicio
while x <= fim:
     print('%d x %d = %d' % (n, x, n * x))
    #print(' {} x {} = {}'.format(n, x, n * x))
    #print(f'{n} x {x} = {n * x}')
     x += 1