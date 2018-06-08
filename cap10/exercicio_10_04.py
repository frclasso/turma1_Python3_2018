#!/usr/bin/env python3

# -*-coding:utf-8 -*-


class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if(self.canal-1 >= self.cmin):
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if(self.canal+1 <= self.cmax):
            self.canal += 1
        else:
            self.canal = self.cmin


tv=Televisao()
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
