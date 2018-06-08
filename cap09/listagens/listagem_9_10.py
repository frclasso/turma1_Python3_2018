#!/usr/bin/env python
# -*-coding:utf-8 -*-
filmes = {
     "drama": ["Cidadão Kane","O Poderoso Chefão"],
     "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
     "policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
     "guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]}
pagina = open("filmes.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
     pagina.write("<h1>{}</h1>".format(c))
     for e in v:
         pagina.write("<h2>{}</h2>\n".format(e))
pagina.write("""
</body>
</html>
""")
pagina.close()
