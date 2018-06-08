#!/usr/bin/env python3
# -*-coding:utf-8 -*-

pagina = open("pagina2.html", "w", encoding="utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Título da Página</title>
</head>
<body>
Olá!
""")
for l in range(10):
    pagina.write("<p>%d</p>\n" % l)
pagina.write("""
</body>
</html>
""")
pagina.close()
