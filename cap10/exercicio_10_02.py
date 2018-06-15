#!/usr/bin/env python3

# -*-coding:utf-8 -*-


class Televisao:
    def __init__(self, canal_inicial, min, max):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if(self.canal -1 >= self.cmin):
            self.canal -= 1

    def muda_canal_para_cima(self):
        if(self.canal +1 <= self.cmax):
            self.canal += 1

            
tv =Televisao(5 ,1 ,99)

print(tv.canal)
