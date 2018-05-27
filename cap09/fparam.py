import sys

print('Numero de parametros: {}'.format(len(sys.argv)))

for n, p in enumerate(sys.argv):
    print('Parametro {} = {}'.format(n,p))