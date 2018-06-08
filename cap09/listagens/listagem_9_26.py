""" Árvore de diretórios sendo percorrida

 Chamar pela linha oe comando:
 python nomedoprograma.py  diretorio
"""
import os
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
     print("\nCaminho:", raiz)
     for d in diretorios:
         print("   %s/" % d)
     for f in arquivos:
         print("   %s" % f)
     print("%d diretório(s), %d arquivo(s)" % (len(diretorios), len(arquivos)))