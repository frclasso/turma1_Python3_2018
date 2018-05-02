#!/usr/bin/env python3

inventory = {'Sword': {'attack': 5, 'defence': 1,
                       'weight':15, 'price': 2},

             'Armor':{'attack':0, 'defence': 10,
                      'weight':25, 'price': 5}
             }


for name, item in inventory.items():
    print('{0}: {1[attack]} {1[defence]} {1[weight]} {1[price]}'.format(name, item))

