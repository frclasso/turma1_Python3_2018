l = [30, 50, 10, 35, 70, 45, 80, 100, 22]

tam_l = len(l)
#bubble sort

for i in range(tam_l):
    for j in range(1, tam_l -i):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]

print(l)