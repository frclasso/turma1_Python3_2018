try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite segundo numero: '))
    print("{} '/' {} '='{}".format(a,b, a/b))
except (ZeroDivisionError, TypeError) as e:
    print('Segundo numero nao pode ser zero!', e)