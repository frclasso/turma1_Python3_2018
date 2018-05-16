"""Exercício 6.11​ Modifique o programa da listagem 6.15 usando ​for​.
 Explique porque nem todos os ​while​ podem ser transformados em ​for​.

Listagem 6.15"""
# L = []
# while True:
#      n = int(input("Digite um número (0 sai):"))
#      if n == 0:
#          break
#      L.append(n)
# x = 0
# while x < len(L):
#      print(L[x])
#      x = x + 1

L = []
while True:
     n = int(input("Digite um número (0 sai):"))
     if n == 0:
         break
     L.append(n)
for e in L:
    print(e)