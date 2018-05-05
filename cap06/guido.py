table = {'Python':'Guido van Rossum', 'Perl':'Larry Wall','TCL':'John Ousterhout'}
language = 'Python'
creator = table[language]
print(creator)

print()

for lang in table.keys():
    print(lang, '\t', table[lang])

print(table.get('Java'))