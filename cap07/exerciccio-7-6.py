'''
Exercício 7.6​ Escreva um programa que leia três strings. Imprima o resultado
da substituição na primeira, dos caracteres da segunda pelos da terceira.
1a string: AATTCGAA
2a string: TG
3a string: AC
Resultado: AAAACCAA
'''

str1 = 'AATTCGAA '
str2 ='TG'
str3 = 'AC'

if len(str2) == len(str3):
    resultado =''
    for letra in str1:
        posicao = str2.find(letra)
        if posicao != -1:  # -1 significa nao encontrado
            resultado += str3[posicao]
        else:resultado+= letra

    if resultado == '':print('Caracteres removidos')
    else:print(f'Os caracteres {str2} foram substituidos por {str3} em {str1}, '
               f'gerando:{resultado}.')
else:print('ERRO, a str2 e str3 devem ter o mesmo tamanho.')


#testar com replace()
print(str1.replace('TG', 'AC'))