fo = open('foo2.txt', 'r+')
print('Nome: ',fo.name)
str = 'sexta linha'
fo.seek(0, 2)
line = fo.write(str)
fo.seek(0,0)
for index in range(6):
    line = next(fo)
    print(f'Linha No: {index} - {line} ')

fo.close()