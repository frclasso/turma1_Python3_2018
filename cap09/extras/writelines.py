fo = open('foo2.txt', 'r+')
print('Nome: ',fo.name)
seq = ['setima linha\n','oitava linha']
fo.seek(0, 2)
line = fo.writelines(seq)

fo.seek(0,0)
for index in range(7):
    line = next(fo)
    print(f'Linha No: {index} - {line} ')

fo.close()