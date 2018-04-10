#!/usr/bin/env python3

prato = 5
pilha = list(range(1, prato+1))

while True:
    print(f'Existem {len(pilha)} pratos na pilha.')
    print('Pilha atual: ', pilha)
    print('Digite E para empilhar novo prato, D para desempilhar ou S para sair')
    operacao = input('Operacao(E, D ou S):')
    if operacao == 'D':
        if(len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print(f'Prato {lavado} lavado')
        else:
            print('Pilha vazia, nada para lavar.')
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao =="S":
        break
    else:
        print('Operacao invalida, Digite apenas E, D ou S')