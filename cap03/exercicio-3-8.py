"""Exercício 3.8  Escreva um programa que leia um valor
em metros e o exiba convertido em milímetros."""

metro = float(input("Digite o valor em metros: "))
milimetros = metro * 1000
print(" %.f metros equivalem a %8.f milimetros" % (metro, milimetros))