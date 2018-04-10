#!/usr/bin/env python3

'''Exercício 5.13  Escreva um programa que pergunte o valor inicial
 de uma dívida e o juros mensal. Pergunte também o valor mensal que
 será pago. Imprima o número de meses para que a dívida seja paga,
 o total pago e o total de juros pago.'''

divida=float(input('Divida: '))
taxa=float(input('Taxa de juros:'))
pagamento=float(input('Pagamento mensal: '))
mes = 1
if(divida * (taxa/100) > pagamento):
    print('Erro, valor invalido')
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa /100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print('Saldo da divida no mes %d eh de R$%6.2f.' % (mes, saldo))
        mes = mes + 1 # podia ser 'mes += 1'
    print('Para pagar a divida de R$%6.2f, a %.f %% de juros' % (divida, taxa))
    print('Sao necessarios %d meses, pagando um total de '
          'R$%6.2f de juros' % (mes -1, juros_pago))
    print('Saldo residual de R$%6.2f a pagar' % (saldo))

