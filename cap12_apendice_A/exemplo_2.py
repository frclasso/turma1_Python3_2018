try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite segundo numero: '))
    print("{} '/' {} '='{}".format(a,b, a/b))
except ZeroDivisionError:
    print('Segundo numero nao pode ser zero!')
except TypeError:
    print('Valor fornecido nao eh um numero inteiro.')
except:
    print('Erro desconhecido.')