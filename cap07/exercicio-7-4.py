'''Exercício 7.4​ Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC Resultado:
T: 2x
A: 2x
C: 1x'''


str = 'TTAAC'
contador = {}
for letra in str:
    if letra in contador:
        contador[letra]+=1
    else:contador[letra]=1

for k in contador:
    print(f'{k}:{contador[k]}x')

print('Usando o count()')

print('T','{}x'.format(str.count('T')))
print('A', '{}x'.format(str.count('A')))
print('C',  '{}x'.format(str.count('C')))
