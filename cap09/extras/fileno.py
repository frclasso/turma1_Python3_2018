fo = open('foo.txt', 'wb')
print('Nome: ', fo.name)

fid = fo.fileno()
print('Descritor: ', fid)

fo.close()