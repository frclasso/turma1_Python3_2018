'''A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
The main difference between the tuples and the lists is that the tuples cannot be changed
unlike lists. Tuples use parentheses, whereas lists use square brackets.
Creating a tuple is as simple as putting different comma-separated values. Optionally, you
can put these comma-separated values between parentheses also.'''

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,2,3,4,5)
tup3 = 'a', 'b', 'c', 'd', 'e'
print(type(tup1),',', type(tup2),',', type(tup3))

'''Esvaziando uma tupla'''
tup1 = ()
print(tup1)

tup1 = (50, ) # escrevendo uma tupla com um unico valor necessario incluir uma virgula
# print(tup1)

'''Acessando valores'''
# print(tup2[0])
# print(tup2[1:5])

'''Updanting Tuples'''
# print(tup1)
# print(tup2)
# tup4 = tup1 + tup2  # concatenacao
# print(tup4)

'''Deletando elementos de uma tupla
   Nao e possivel deletar elementos individualmente.'''
# print('tup4')
# print(tup4)
# del tup4
#print(tup4)  # NameError: name 'tup4' is not defined

'''Operacoes basicas'''
# print(len(tup2))
#
# tup5 = tup1+tup2+tup3
# print(tup5) # concatenacao
#
# print((tup1) * 4) #repeticao
#
# print(3 in tup2) # Operador in verifica se 3 eh membro de tup2
#
# for x in tup2:print(x, end=',') # interacao
# print()


'''Indices, Fatias e Matriz'''

# T = ('C++', 'Java', 'Python')
# print(T[2])
# print(T[-2])
# print(T[1:])

'''len() method'''
tupla1, tupla2 = (123, 'xyz', 'zara'), (456, 'abc')
print('First tuple length: ', len(tupla1))
print('Second tuple length: ', len(tupla2))

'''max() method'''
tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
print('Max value element: ', max(tuple1))
print('Max value element: ', max(tuple2))

'''min() method'''
print('Min value element: ', min(tuple1))
print('Min value element: ', min(tuple2))

'''tuple() methods -  converts a list into tuples '''

lista1 = ['maths','che', 'phy', 'bio']
novaTupla = tuple(lista1)
print(novaTupla, type(novaTupla))