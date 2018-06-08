#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""Listagem do nome de arquivos e diretórios
"""

import os, sys

print(os.listdir("."))
print(os.listdir("avo"))
print(os.listdir("avo/pai"))
print(os.listdir("avo/mãe"))
print('Comando tree do Linux:')
print(os.system('tree'))