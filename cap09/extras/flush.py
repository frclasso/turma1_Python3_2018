import os
fo= open('foo.txt', 'wb')
print('Nome do arquivo: ', fo.name)

fo.flush()
fo.close()