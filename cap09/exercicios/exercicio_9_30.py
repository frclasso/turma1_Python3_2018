"""Modifique o programa da listagem 9.10 para gerar uma lista html,
usando os elementos <ul> e <li>. Todos os elementos da lista devem
estar dentro do elemento <ul>, e cada item dentro de um elemento <li>.
Exemplo:
<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>"""

filmes = {
     "drama": ["Cidadão Kane","O Poderoso Chefão"],
     "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
     "policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
     "guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]}

pagina = open("filmes2.html","w", encoding = "utf-8")
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
    pagina.write("<h1>%s</h1>\n\n" % c.capitalize())
    pagina.write("<ul>\n")
    for e in v:
        pagina.write("\t<li>%s</li>\n" % e)
    pagina.write("</ul>\n\n")
pagina.write("""
</body>
</html>
""")
pagina.close()
