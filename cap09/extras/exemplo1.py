#!/usr/bin/env python3

# -*-coding:utf-8 -*-

fo = open('foo.txt', 'w')
print('Nome do arquivo: ', fo.name)
print('Fechado?', fo.closed)
print('Modo?', fo.mode)
fo.close()