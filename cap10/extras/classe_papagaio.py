#!/usr/bin/env python3

# -*-coding:utf-8-*-


class Papagaio:

    # atributo de classe
    species = "bird"

    # atributo de instancia
    def __init__(self, name , age):
        self.name = name
        self.age = age


# instanciando objetos
blu = Papagaio('Blu', 10)
woo = Papagaio('Woo', 15)

# acessando atributos de classe
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

# acessando atributos de objetos
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))