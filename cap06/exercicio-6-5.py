#!/usr/bin/env python3


ultimo = 10
fila = list(range(1, ultimo+1))

while True:
    print(f'Existem {len(fila)} clientes na fila.')
    print('Fila atual:', fila)
    print('Digite F para adicionar um cliente ao fim da fila.')
    print('ou A para realizar um Atendimento. S para sair.')

    operacao = input('Operacao(F,A,ou S): ')
    if operacao == "A":
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print('Cliente {} atendido'.format(atendido))
        else:
            print('Fila vazia, ninguem para antender.')
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print('Operacao invalida. Digite apenas F,A ou S.')