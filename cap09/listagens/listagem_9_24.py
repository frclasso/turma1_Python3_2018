"""Uso de caminhos"""

import os.path
caminho = "avo/pai/filho/netos"
print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext("arquivo.txt"))
print(os.path.splitdrive("c:/Windows"))