fo = open('foo.txt', 'r')
print('Nome: ',fo.name)
for index in range(4):
    line = next(fo)
    print(f'Line No {index} - {line}')