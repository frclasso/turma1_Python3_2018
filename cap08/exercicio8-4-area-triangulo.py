'''Exercício 8.4 - Escreva uma função que receba a base e a altura de um triângulo e
retorne sua área (A = (base x altura)/2).
Valores esperados: area_triangulo(6,9) == 27
                   area_triangulo(5,8) == 20
'''


def area_do_triang(base, altura):
    return (base * altura)/2

print(f'Area do triangulo(6,9) == 27 => obtido: {area_do_triang(6,9)}')
print(f'Area do triangulo(5,8) == 20 => obtido: {area_do_triang(5,8)}')
