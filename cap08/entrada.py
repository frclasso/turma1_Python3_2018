def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print(f'Digite um valor entre {maximo} e {minimo}.')
        except: print('Voce deve digitar um numero inteiro.')