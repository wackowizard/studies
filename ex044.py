try:
    preço = float(input('O valor do produto, em reais: R$'))

    print('FORMAS DE PAGAMENTO')
    print('1 - À vista em dinheiro ou cheque (10% de desconto)')
    print('2 - À vista no cartão (5% de desconto)')
    print('3 - Em até 2x no cartão (preço normal, sem juros).')
    print('4 - Em 3x ou mais no cartão (20% de juros)')
    escolha = int(input('Digite apenas o número da forma de pagamento escolhida: '))

    if escolha == 1:
        print(f'Com 10% de desconto, agora o valor é R${preço * 0.90:.2f}')
    elif escolha == 2:
        print(f'Com desconto de 5% de desconto, agora o valor é R${preço * 0.95:.2f}')
    elif escolha == 3:
        print(f'Em duas vezes, o valor de cada parcela fica R${preço / 2:.2f}')
    elif escolha == 4:
        numero_de_parcelas = int(input('Em até 12 parcelas, em quantas quer pagar? '))
        if numero_de_parcelas <= 12:
            print(f'Em {numero_de_parcelas}x, cada parcela fica no valor de R${(preço * 1.20) / numero_de_parcelas:.2f} com juros. Valor total: {preço * 1.20}')
        if numero_de_parcelas > 12:
            print('Valor inválido. O máximo são 12 parcelas para esta compra.')
    else:
        print('ERRO: Insira um número válido!')
except:
 print('ERRO: Insira um número válido!')