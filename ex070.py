print('=' * 20)
print('LOJA SUPER BARATÃO')
print('=' * 20)

soma = produtos_caros = 0
barato_nome = ''
barato_valor = float('inf')

while True:
    while True:
        produto = input('Nome do Produto: ').strip()
        if produto:
            break
        else:
            print('Nome não pode estar vazio. Tente novamente.')

    while True:
        preco_str = input('Preço: R$').strip().replace(',', '.')
        try:
            preco = float(preco_str)
            if preco >= 0:
                break
            else:
                print('Digite um valor positivo.')
        except ValueError:
            print('Valor inválido. Tente novamente...')

    soma += preco
    if preco > 1000:
        produtos_caros += 1

    if preco < barato_valor:
        barato_valor = preco
        barato_nome = produto

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('Insira uma resposta correta, S ou N.')

    if continuar == 'N':
        break

print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {produtos_caros} produtos custando mais de R$1.000')
print(f'O produto mais barato foi {barato_nome} que custa R${barato_valor:.2f}')


#como daria pra fazer também
'''total = totmil = menor = cont = 0
barato = ''

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
'''