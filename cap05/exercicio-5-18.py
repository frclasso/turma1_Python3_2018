'''Exercício 5.18  Modifique o programa para também
trabalhar com notas de R$100.'''

# listagem 5.14  - contagem de cedulas

valor = int(input('Digite valor a pagar: '))
cedulas = 0
#atual = 50
atual = 100
apagar= valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cedulas de R${atual}')
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.1
        cedulas = 0