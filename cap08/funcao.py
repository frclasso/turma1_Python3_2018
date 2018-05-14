#!/usr/bin/env python3
"""O objetivo deste exemplo eh apresentar o padrao de chamada de funcao atraves
da funcao main(), padrao bastante empregado."""

def soma_de_numeros(a,b):
    print('Soma:')
    print(a + b)


def subtracao(a,b):
    print('Subtacao: ')
    print(a -b)


def multiplicacao(a, b):
    print('Multiplicaoca: ')
    print(a * b)


def divisao_exata(a, b):
    print('Divisao exata:')
    print(a//b)


def imprimir():
    print('Algumas operacoes matematicas simples!!')


def main():
    imprimir()
    soma_de_numeros(4,8)
    subtracao(4,2)
    multiplicacao(2,3)
    divisao_exata(6,2)


if __name__=="__main__":main()
