'''Exercício 7.3​ Escreva um programa que leia duas strings e
 gere uma terceira apenas com os caracteres que aparecem em uma delas.
1a string: CTA
2a string: ABC
3a string: BT
A ordem dos caracteres da terceira string não é importante.
'''

str1 ='CTA'
str2 ='ABC'
str3=''

for letra in str1:
    if letra not in str2 and letra not in str3:
        str3+=letra
for letra in str2:
    if letra not in str1 and letra not in str3:
        str3+=letra
if str3 == '':print('Caracteres nao encontrados')
#else: print('Caracteres incomuns: ', str3)
else: print('Caracteres incomuns: ', sorted(str3))