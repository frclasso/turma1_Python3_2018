'''Copia de elementos para outra lista'''

V = [9,8,7,12,0,13,21]
p =[]
i =[]

for e in V:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)

print(p)
print(i)