try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite segundo numero: '))
    print("{} '/' {} '='{}".format(a,b, a/b))
except ZeroDivisionError as e:
    print('Segundo numero nao pode ser zero!')
except TypeError as e :
    print('Valor fornecido nao eh um numero inteiro.', e)
except Exception as e :
    print('Erro nao identificado', e)
    raise