'''Exercício 7.2 ​Escreva um programa que leia duas strings e gere uma
terceira com os caracteres comuns às duas lidas.
1a string: AAACTBF 2a string: CBT Resultado: CBT'''

str1 = 'AAACTBF'
str2 = 'CBT'
str3 = ''

for letra in str1:
    if letra in str2 and letra not in str3:
        str3 += letra
if str3 == '':print('Caracteres comuns nao encontrados')
else:print(f'Caracteres comuns: {str3}')