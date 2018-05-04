'''Dicionario com estoque e operacoes de venda'''

estoque = {'Alface': [500,0.45],
          'Batata': [2001,1.20],
          'Tomate':[500,2.30],
          'Feijao':[100,1.50]
          }

venda = [['Tomate', 5],
         ['Batata', 10],
         ['Alface', 5]]
total = 0
print('Vendas:\n')
for operacao in  venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'Produto: {produto} //  Qtd: {quantidade} x R${preco} = R${custo}')
    estoque[produto][0]-=quantidade
    total+=custo
print()
print(f'Custo total R${total}')
print(f'Estoque {estoque}')
print()
for chave, dados in estoque.items():
    print(f'Descricao: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preco: R$ {dados[1]}')
