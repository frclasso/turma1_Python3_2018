"""Modifique o programa da listagem 9.20 de forma a receber o
nome do arquivo ou diretório a verificar pela linha de comando.
Imprima se existir e se for um arquivo ou um diretório."""

import sys
import os.path

if len(sys.argv)<2:
    print("Digite o nome do arquivo ou diretório a verificar como parâmatro!")
    sys.exit(1)

nome = sys.argv[1]
if os.path.isdir(nome):
     print("O diretório %s existe." % nome)
elif os.path.isfile(nome):
    print ("O arquivo %s existe." % nome)
else:
     print("%s não existe." % nome)
