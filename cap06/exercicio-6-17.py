'''Exercício 6.17​ Altere o programa da listagem 6.53 de forma a solicitar
 ao usuário o produto e a quantidade vendida. Verifique se o nome do produto
digitado existe no dicionário, e só então efetue a baixa em estoque.'''

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


while True:
    produto = input('Digite o nome do produto (fim para sair): ')
    if produto == 'fim':break
    if produto in estoque:
        quantidade = int(input('Quantidade: '))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f'Produto: {produto} //  Qtd: {quantidade} x R${preco} = R${custo}')
            estoque[produto][0]-=quantidade
            total+=custo
        else: print('Quantidade indisponivel!!!')
    else: print('Nome do produto invalido.')
print()
print(f'Custo total R${total}')
print(f'Estoque {estoque}')
print()
for chave, dados in estoque.items():
    print(f'Descricao: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preco: R$ {dados[1]}')
