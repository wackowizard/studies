listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

produtos = listagem[0::2]
precos = listagem[1::2]

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for nome, preco in zip(produtos, precos):
    print(f'{nome:.<30}R$ {preco:>7.2f}')

print('-' * 40)