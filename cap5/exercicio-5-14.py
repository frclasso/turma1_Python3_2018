'''Exercício 5.14  Escreva um programa que leia números inteiros do teclado.
 O programa deve ler os números até que o usuário digite 0 (zero).
 No final da execução, exiba a quantidade de números digitados,
 assim como a soma e a média aritmética.'''

soma = 0
quantidade = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print('Quantidade de numeros digitados: ', quantidade)
print('Soma: ',soma)
print('Media: %.f ' % (soma/quantidade))

