fo = open('foo.txt', 'r+')
str = fo.read(10)
print('Lendo string:', str)

position = fo.tell()
print('Posicao atual: ', position)

position = fo.seek(0, 0)
print("Posicao atual depois do seek:", position)
str = fo.read(20)
print('Novamente, lendo a string: ', str)

position = fo.tell()
print('Posicao final: ', position)

fo.close()