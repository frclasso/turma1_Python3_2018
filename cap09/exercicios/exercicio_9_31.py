#!/usr/bin/env python3

"""Criem um programa que corrija o da listagem 9.20 de forma a
verificar se “z” existe e é um diretório.
"""
import os.path
if os.path.isdir("z"):
     print("O diretório z existe.")
elif os.path.isfile("z"):
    print ("z existe, mas é um arquivo e não um diretório.")
else:
     print("O diretório z não existe.")