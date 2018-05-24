a = 5


def muda_valor():
    global a
    a = 7
    print(f'"a" dentro da funcao: {a}')
muda_valor()
print(f'Fora da funcao: {a}')