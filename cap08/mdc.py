'''Exercício 8.7 ​ Defina uma função recursiva que calcule o maior divisor
 comum (MDC) entre dois números “a” e “b”, onde “a > b”.
(fórmulas página 172 do livro)'''


def mdc(dividendo,divisor):
    if divisor == 0:
        return dividendo
    return mdc(divisor, dividendo % divisor)

print(f'MDC 10 e 5 ==> {mdc(10, 5)}')
print(f'MDC 32 e 24 ==> {mdc(32, 24)}')
print(f'MDC 5 e 3 ==> {mdc(5, 3)}')