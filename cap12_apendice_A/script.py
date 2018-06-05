import sys

randomList = ['a', 0, 2]

for entrada in randomList:
    try:
        print('A entrada eh:', entrada)
        r = 1/entrada
        break
    except:
        print('Opa!', sys.exc_info()[0], 'ocorreu.')
        print('Proxima entrada.')
        print()
print('O reciproco de ', entrada, 'eh', r)