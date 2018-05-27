def imprime_maior(msg, *numeros):
    maior = None
    for e in numeros:
        if maior == None or maior < e:
            maior = e
    print(msg, maior)

imprime_maior("Maior: ", 5,4,3,2,1)
imprime_maior("Max: ", *[1,7,9])
imprime_maior("Max")