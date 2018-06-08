#! -*-coding:utf-8 -*-

import os
os.mkdir("d")
os.mkdir("e")
os.mkdir("f")
print(os.getcwd())
os.chdir("d")
print(os.getcwd())
os.chdir("../e")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("f")
print(os.getcwd())


"""Criação de diretórios"""