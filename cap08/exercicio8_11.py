'''Exercício 8.11 ​Escreva uma função para validar uma variável string.
 Essa função recebe como parâmetro a string, o número mínimo e máximo
 de caracteres. Retorne verdadeiro se o tamanho da string estiver entre
  os valores de máximo e mínimo, e falso em caso contrário.'''


def valida_string(string, minimo,maximo):
    tamanho = len(string)
    return minimo <= tamanho <= maximo

print(f'Validando a string Python, minimo 2 e maximo 5:'
      f' {valida_string("Python",2,6)}')


print(f'Validando a string Python, minimo 2 e maximo 5:'
      f' {valida_string("Algoritmo",2,5)}')