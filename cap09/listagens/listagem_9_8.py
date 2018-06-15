#!/usr/bin/env python3

# -*-coding:utf-8 -*-

pagina = open("pagina.html","w", encoding = "utf-8")
pagina.write("<!DOCTYPE html>\n")
pagina.write("<html lang=\"pt-BR\">\n")
pagina.write("<head>\n")
pagina.write("<meta charset=\"utf-8\">\n")
pagina.write("<title>Título da Página</title>\n")
pagina.write("</head>\n")
pagina.write("<body>\n")
pagina.write("Olá!")
for l in range(10):
    pagina.write("<p>%d</p>\n" % l)
pagina.write("</body>\n")
pagina.write("</html>\n")
pagina.close()
