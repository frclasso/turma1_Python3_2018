#!/usr/bin/env python3

# -*-coding:utf-8 -*-

""" Exclusão de arquivos e diretórios
"""
import os
# Cria um arquivo e o fecha imediatamente
open("morimbundo.txt","w").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("morimbundo.txt")
print('Arquivo removido com sucesso!')