def media(L):
    total = 0
    for e in L:
        total+=e
    return total/len(L)

L=[1,2,3,4,5]
print(media(L))