'''Exercício 8.2 - Escreva uma função que receba dois números e retorne
True se o primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8,4) == True
múltiplo(7,3) == False
múltiplo(5,5) == True'''


def multiplos(a, b):
    return a % b == 0


def main():
    print(f'Múltiplo(8,4) == True, obtido: {multiplos(8, 4)}')
    print(f'Múltiplo(7,3) == False, obtido: {multiplos(7, 3)}')
    print(f'Múltiplo(5,5) == True, obtido: {multiplos(5, 5)}')


if __name__=="__main__":main()