class Item(object):
    def __init__(self, nome, quantidade, peso,  preco):
        self.nome = nome
        self.quantidade = quantidade
        self.peso = peso
        self.preco = preco


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.nome] = item

    def print_items(self):
        print('\t'.join(['Nome', 'Qtd', 'Peso', 'Preco']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.nome, item.quantidade, item.peso, ' ','R$',item.preco]]))


inventory = Inventory()
inventory.add_item(Item('Maca', 5, 1, 15))
inventory.add_item(Item('Pera', 0, 10, 25))
inventory.add_item(Item('Abacaxi', 0, 10, 25))

inventory.print_items()