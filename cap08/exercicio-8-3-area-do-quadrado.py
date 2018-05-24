'''Exercício 8.3 - Escreva uma função que receba o lado (1) de um quadrado e
retorne sua área (A = lado2​ ​).
Valores esperados:
area_quadrado(4) == 16
area_quadrado(9) == 81'''


def area_quadrado(lado):
    return lado ** 2


def area_qdo2(a,b):
    'Retorna valor utilizando a funcao interna pow(power) com dois parametros'
    return pow(a,b)


def main():
    print(f'Area do quadrado(4) eh: {area_quadrado(4)}')
    print(f'Area do quadrado(9) eh: {area_quadrado(9)}')
    print(area_qdo2.__doc__)
    print(f'Area do quadrado2:  {area_qdo2(4,2)}')


if __name__=="__main__":main()

