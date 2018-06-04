fo = open('foo2.txt', 'r+')

print('Nome: ',fo.name)

# line = fo.read(9)
# print('Linha: ', line)
#
# print('Read line')
# line = fo.readline(5)
# print('Lendo a linha: ', line)

print('Read lines')
line = fo.readlines()
print('Lendo a linha: ', line)

line = fo.readlines(2)
print('Lendo a linha: ', line)


fo.close()