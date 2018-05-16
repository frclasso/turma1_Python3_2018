'''Exercício 7.5​ Escreva um programa que leia duas strings e gere uma terceira,
 na qual os caracteres da segunda foram retirados da primeira.
1a string: AATTGGAA
2a string: TG
3a string: AAAA'''

str1 ='AATTGGAA'
str2='TG'
str3 =''

for letra in str1:
    if letra not in str2:
        str3 += letra

if str3 == '':print('Caracteres foram retirados da primeira')
else:print(f'Caracteres removidos {str2}, de {str1} gerando {str3}.')

#Utilizando set()
# str4 = set('AATTGGAA')
# str5 = set('TG')
# str6 = {x for x in str4 if x not in str5}
# print(str6)