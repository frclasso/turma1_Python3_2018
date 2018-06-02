#!/usr/bin/env python3

# -*_coding: utf-8 -*-

impares = open('impares.txt', 'w')
pares = open('pares.txt', 'w')
for n in range(0, 1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        impares.write("%d\n" % n)

impares.close()
pares.close()