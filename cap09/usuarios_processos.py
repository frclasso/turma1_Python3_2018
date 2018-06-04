import os

print('Retorna id do usuario atual:{} '.format(os.getuid()))
print('Retorna id do grupo atual: {}'.format(os.getgid()))
print('Retorna id do  processo atual: {}'.format(os.getpid()))
print('Retorna id do  processo Pai : {}'.format(os.getppid()))

print('Qual seu sistema operacional? {}'.format(os.uname()))
print('Diretorio atual: {}'.format(os.getcwd()))
print('Verificando se diretorio extras existe: {}'.format(os.path.isdir('extras')))

print('Verificando se arquivo foot.txt existe: {}'.format(os.path.isfile('foo.txt')))
print('Verificando o tamanho do arquivo: {} mb.'.format(os.path.getsize('foo.txt')))

import time
