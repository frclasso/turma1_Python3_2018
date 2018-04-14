def retângulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)


retângulo(3, 4)
retângulo(largura=3, altura=4)
retângulo(altura=4, largura=3)
retângulo(caractere="-", altura=4, largura=3)