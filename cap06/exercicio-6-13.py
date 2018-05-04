"""
Exercício 6.13​ - A lista de temperaturas de Mons, na Bélgica, foi armazenada na
 lista T = [-10, -8, 0, 1,2,5,-2,-4]. Faça um programa que imprima a menor e a
  maior temperatura, assim como a temperatura média.

"""

T = [-10, -8, 0, 1,2,5,-2,-4]
temp_min = T[0]
temp_max = T[0]

soma = 0

for e in T:
    if e < temp_min:
        temp_min = e
    if e > temp_max:
        temp_max = e
    soma +=e
print('Temperauta maxima {}'.format(temp_max))
print('Temperauta minima {}'.format(temp_min))
print('Temperauta media {}'.format(soma / len(T)))
print()


print('Temperatura maxima: {}'.format(max(T)))
print('Temperatura minima: {}'.format(min(T)))
