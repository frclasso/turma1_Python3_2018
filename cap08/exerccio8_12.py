'''Exercício 8.12 ​Escreva uma função que receba uma string e uma lista.
A função deve comparar a string passada com os elementos da lista, também
 passada como parâmetro. Retorne verdadeiro se a string for encontrada
 dentro da lista, e falso em caso contrário.'''


def procura_string(s, lista):
    if s in lista:
        return True, s
    else: return False

L = ['AB', 'CD', 'EF', 'FGH']

print(procura_string('AB', L))
print(procura_string('cd', L))
print(procura_string('EF', L))
print(procura_string('FG', L))