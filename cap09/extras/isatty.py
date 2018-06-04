fo = open('foo.txt', 'wb')
print('Nome: ', fo.name)
r = fo.isatty()
print('Conectado em um terminal? ', r)

fo.close()