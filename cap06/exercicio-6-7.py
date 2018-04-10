"""Exercício 6.7  Faça um programa que leia uma expressão com parênteses.
Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.

Exemplo:
( () ) ok
() () ( () () ) ok ()) Erro"""

expressao = input('Digite a sequencia de paranteses a validar: ')
x = 0
pilha =[]
while x< len(expressao):
    if expressao[x] == "(":
        pilha.append("(")
    if expressao[x] == ")":
        if len(pilha)>0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x+=1
# if(len(pilha)==0):
#     print('ok')
# else:
#     print('Erro')
print('OK')if(len(pilha) == 0) else print('Erro')