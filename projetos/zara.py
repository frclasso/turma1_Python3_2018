dicionario ={'Name':'Zara', 'Age': 20}
print(dicionario['Name'])
print(dicionario['Age'])
dicionario['Class'] ='First'  # inserindo elementos
print(dicionario)
dicionario['Age'] = 21 #atualizando
dicionario['School'] = 'DPS' # inserindo elementos
# print(dicionario['Age'])
# print(dicionario['School'])

#deletando elementos de um dicionario
#del dicionario['Name']
# print(dicionario)
#
# # removendo todos os item de um dicionario
# dicionario.clear()
# print(dicionario)
#
# # deletando todo dicionario
# del dicionario
# print(dicionario) # Erro => Traceback (most recent call last):print(dicionario)
                            #  NameError: name 'dicionario' is not defined

'''imprimindo dicionario utlizando str'''

# print('String equivalente: ',str(dicionario))
# newDict = dicionario.copy()
# print(f'Novo dicionario: {newDict}')


''' fromkeys() Method - creates a new dictionary with keys from seq and values
                        set to value.
                        sintax: dict.fromkeys(seq[, value])
'''

# seq = ('name', 'age', 'sex')
# d = dict.fromkeys(seq)
# print(f'New Dictionary: {str(d)}')
# d = dict.fromkeys(seq, 10)
# print(f'New Dictionary: {str(d)}')

"""get() method - returns a values for the given key or None if the key not exist.
                  sintax: dict.get(key, default=None)"""
# print(dicionario)
# print('Values: {}'.format(dicionario.get('Age')))
# print('Values: {}'.format(dicionario.get('Sex')))
# print('Values: {}'.format(dicionario.get('Sex', 'N/A')))  # passando valor como parametro

'''items() - returns a list of tuple pairs'''
#print(dicionario.items())


'''key()  - returns a list of all available keys in the dictionary'''

#print(dicionario.keys())

'''setdefault() - is similar get(), but will set dict[key]=default if 
the key is not already in dict. sintax: dict.setdefault(key, default=None)'''

print(dicionario.setdefault('Age', None))
print(dicionario.setdefault('Color'))
print(dicionario)
dicionario2 = {'Phone': 99998888}
dicionario.update(dicionario2)
#print(f'Dicionario atualiado via dicionario2: {dicionario}')

#values()
print(dicionario.values())

