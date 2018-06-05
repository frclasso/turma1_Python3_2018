try:
    try:
        x = int(input('Digite um numero: '))
    finally:
        print('Reestabelecendo um novo valor para x.')
        x = None
except:
    print('Ocorreu algum erro.')
