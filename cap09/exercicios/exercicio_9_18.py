"""O que acontece se o nome ou telefone contiverem o caractere usado com separador em seus conteúdos?
Explique o problema e proponha uma solução.

Resposta:
Se o # aparecer no nome ou telefone de uma entrada na agenda,
ocorrerá um erro ao ler o arquivo.
Este erro ocorre pois o número de campos esperados na linha será diferente
de 2 (nome e telefone).
O programa não tem como saber que o caracter faz parte de um campo ou de outro.
Uma solução para este problema é substituir o # dentro de um campo antes de salvá-lo.
Desta forma, o separador de campos no arquivo não seria confundido com o conteúdo.
Durante a leitura a substituição tem que ser revertida, de forma a obter o mesmo conteúdo."""

