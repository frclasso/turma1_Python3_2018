def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f'Valor invalido. Digite valor entre {minimo} e {maximo}')
            return max(minimo,maximo)


print(faixa_int('Quais valores?', 1, 5))