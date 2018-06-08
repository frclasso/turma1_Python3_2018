"""Utilizando a função ​os.walk()​, crie uma página HTML com o nome e tamanho
 de cada arquivo de um diretório passado e de seus subdiretórios.
"""
# -*- conding:utd-8 -*-

import sys
import os
import os.path
# este módulo ajuda com a conversão de nomes de arquivos para links
# válidos em HTML
import urllib.request

mascara_do_estilo = "'margin: 5px 0px 5px %dpx;'"


def gera_estilo(nivel):
    return mascara_do_estilo % (nivel * 20)


def gera_listagem(pagina, diretorio):
    nraiz = os.path.abspath(diretorio).count(os.sep)
    for raiz, diretorios, arquivos in os.walk(diretorio):
        nivel = raiz.count(os.sep) - nraiz
        pagina.write("<p style=%s>%s</p>" % (gera_estilo(nivel), raiz))
        estilo = gera_estilo(nivel+1)
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            tamanho = os.path.getsize(caminho_completo)
            link = urllib.request.pathname2url(caminho_completo)
            pagina.write("<p style=%s><a href='%s'>%s</a>\n "
                         " (%d bytes)</p>" % (estilo, link, a, tamanho))


if len(sys.argv)<2:
    print("Digite o nome do diretório para coletar os arquivos!")
    sys.exit(1)

diretorio = sys.argv[1]

pagina = open("arquivos.html","w", encoding="utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
pagina.write("Arquivos encontrados a partir do diretório: {}\n" .format(diretorio))
gera_listagem(pagina, diretorio)
pagina.write("""
</body>
</html>
""")
pagina.close()
