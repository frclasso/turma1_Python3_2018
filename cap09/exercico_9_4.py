#!/usr/bin/rnv python3

# -*- coding:utf-8 -*-
import sys

primeiro = open(sys.argv[1], 'r')
segundo = open(sys.argv[2], 'r')
saida = open(sys.argv[3], 'w')

for l in primeiro:
    saida.write(l)
for l2 in segundo:
    saida.write(l2)

primeiro.close()
segundo.close()
saida.close()