#!/usr/bin/env python3

nomeDoArquivo = input('Digite nome do arquivo: ')
try:
    f = open('arquivo.txt', 'r')
except:print('Nao existe este arquivo', nomeDoArquivo)