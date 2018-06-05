while True:
    try:
        a = int(input('Digite um numero: '))
        b = int(input('Digite segundo numero: '))
        print("{} '/' {} '='{}".format(a,b, a/b))
    except Exception as e :
        print('Erro nao identificado', e)
    else:
        break