class Error(Exception):
    """Classe base para outras excecoes"""
    pass


class ValueTooSmallError(Error):
    """Levantada quando  o valor de entrada eh pequeno."""
    pass


class ValueTooLargeError(Error):
    """Levantada quando  o valor de entrada eh grande."""
    pass


"""voce tem que adivinhar este numero"""
number = 10
while True:
    try:
        i_num = int(input('Digite um numero: '))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('Esse valor eh muito pequeno, tente novamente.')
        print()
    except ValueTooLargeError:
        print('Esse valor eh muito grande, tente novamente.')
        print()
print('Parabens, voce adivinhou o numero!')
