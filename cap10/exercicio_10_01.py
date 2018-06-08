#!/usr/bin/env python3

# -*-coding:utf-8 -*-


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Ching-Ling"

tv = Televisao()
tv.tamanho = 27
tv.marca = "LongDang"
tv_sala = Televisao()
tv_sala.tamanho = 52
tv_sala.marca = "XangLa"

print("tv tamanho=%d marca=%s" % (tv.tamanho,tv.marca ))
print("tv_sala tamanho=%d marca=%s" % (tv_sala.tamanho,tv_sala.marca ))