#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""Verificação se e diretório ou arquivo
"""

import os
import os.path
for a in os.listdir("."):  # verifica se eh um diretorio
     if os.path.isdir(a):
         print("%s/" % a)
     elif os.path.isfile(a): #verifica se eh um arquivo
         print("%s" % a)