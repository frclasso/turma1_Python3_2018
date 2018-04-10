# tabuada =1
# while tabuada <= 10:
#     numero = 1
#     while numero <= 10:
#         print('%d x %d = %d' % (tabuada, numero, tabuada * numero))
#         numero +=1
#     tabuada += 1
#
#

tabuada =1
numero = 1
while tabuada <= 10:
    print('%d x %d = %d' % (tabuada, numero, tabuada * numero))
    numero +=1
    if numero == 11:
        numero = 1
        tabuada += 1
