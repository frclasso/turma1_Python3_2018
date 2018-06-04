fo = open('foo2.txt', 'r+')

print('Nome: ',fo.name)

line = fo.readlines()
print('Linha: ', line)

fo.seek(0,0)
line = fo.readline()
print('Linha atual: ', line)

pos = fo.tell()
print('Posicao atual :', pos)
fo.close()
