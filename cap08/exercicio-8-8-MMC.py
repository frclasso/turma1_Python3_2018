'''Exercício 8.8 ​Usando a função MDC definida no exercício anterior,
defina uma função para calcular o menor múltiplo comum
(MMC) entre dois números.
'''
from mdc import mdc

# def mdc(dividendo,divisor):
#     if divisor == 0:
#         return dividendo
#     return mdc(divisor, dividendo % divisor)


def mmc(dividendo, divisor):
    return (dividendo*divisor) / mdc(dividendo,divisor)

print(f'MDC 10 e 5 ==> {mmc(10, 5)}')
print(f'MDC 32 e 24 ==> {mmc(32, 24)}')
print(f'MDC 5 e 3 ==> {mmc(5, 3)}')