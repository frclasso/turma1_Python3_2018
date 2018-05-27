'''Exercício 8.13 ​Altere o programa da listagem 8.37 de forma que o usuário
 tenha três chances de acertar o número. O programa termina se o usuário
acertar ou errar três vezes.'''

import random

n = random.randint(1,10)
tentativas = 0
while tentativas < 3:
    x = int(input('Escolha um numero entre 1 e 10: '))
    if (x == n):
        print('Voce acertou!')
        break
    else:print('Voce errou.')
    tentativas+=1