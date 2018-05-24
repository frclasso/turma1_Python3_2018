def soma(L):
    total=0
    for e in L:
        total+= e
    return total


def soma2(L):
    return sum(L)


def media():
    return (soma(L)/len(L))


L=[1,2,3,4,5]
print(soma(L))
print(media())
print(soma2(L))
