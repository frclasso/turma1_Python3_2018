#!/usr/bin/env python3

previous = {0:1, 1:1}


def fibonacci(n):
    """O dicionário chamado previous guarda os números de Fibonacci que nós ja conhecemos.
    Ele começa com apenas dois pares: 0 possui 1; e 1 possui 1.
    Sempre que fibonacci é chamada, ela verifica o dicionário para determinar se ele já possui
    o resultado. Se o resultado estiver ali, a função pode retornar imediatamente sempre
    precisar fazer mais chamadas recursivas. Se o resultado não estiver ali, ele é calculado
    no newValue. O valor de newValue é adicionado no dicionário antes da função retornar.

    hint
    O armazenamento temporário de um valor pré-computado para evitar a computação redundante."""
    if n in previous:
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n -2)
        previous[n] = newValue
        return newValue


print(f'Fibonacci: ',fibonacci(80))
print(fibonacci.__doc__)
