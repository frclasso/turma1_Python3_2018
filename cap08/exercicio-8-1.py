'''Exercício 8.1 - Escreva uma função que retorne o maior de dois números
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7'''


def maior(a,b):
    # if a > b:return a
    # else:return b
    #return a if a > b else b
    return max(a,b)

def main():
    print(f'Maximo (5,6) eh: {maior(6,5)}')
    print(f'Maximo (2,1) eh: {maior(2,1)}')
    print(f'Maximo (7,7) eh: {maior(7,7)}')


if __name__=="__main__":main()