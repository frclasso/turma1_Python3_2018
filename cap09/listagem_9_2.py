arquivo = open('numeros.txt','r') # r = read/leitura
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
