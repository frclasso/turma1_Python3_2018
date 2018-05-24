'''Exercício 8.6 ​Reescreva o​ ​programa da listagem 8.8 de forma a utilizar ​for
​ em vez do ​while​.

def​ soma(L):
    total = 0
    x= 0
    ​while​ x < 5:
        total += L[x]
        x+=1 ​
    return​ total
L = [1,7,2,9,15]
'''


def soma(L):
    total=0
    for e in L:
        total+= e
    return total


def soma2(L):
    return sum(L)

L = [1,7,2,9,15]
print(f'Imprimindo a soma: {soma(L)}')
print(f'Imprimindo soma 2: {soma2(L)}')