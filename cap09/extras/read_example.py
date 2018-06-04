fo = open('foo.txt', 'r+')
str = fo.read(10)
print('Lendo string:', str)
fo.close()