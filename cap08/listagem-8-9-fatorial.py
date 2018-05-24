
def fatorial(n):
    fat=1
    while n > 1:
        fat *= n  # fat = fat * n
        n -= 1  #  n = n - 1
    return fat


def fatorial2(n):
    import math
    return math.factorial(n)


print(fatorial(3))
print(fatorial(4))
print(fatorial(5))
print(fatorial(6))

print(f'Usando a funcao math.factorial: {fatorial2(6)}')