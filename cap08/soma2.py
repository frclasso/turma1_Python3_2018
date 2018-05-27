#importando entrada.py

from entrada import valida_inteiro
#import entrada

L = []
for x in range(10):
    L.append(valida_inteiro("Digite um numero: ", 0, 20))
print('Soma: {}'.format(sum(L)))