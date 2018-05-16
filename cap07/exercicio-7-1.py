'''Exercício 7.1 ​Escreva um programa que leia duas strings.
Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1a string: AABBEFAATT
2a string: BE'''

str1 = 'AABBEFAATT'
str2 = 'BE'
print('BE' in 'AABBEFAATT')

posicao = str1.find(str2)

if posicao == -1:
    print(f'{str2} nao encontrada em {str1}')
else:
    print(f'{str2} encontrada na posicao {posicao} de {str1}')