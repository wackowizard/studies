try:
    valor_1 = int(input('Digite o primeiro valor inteiro: '))
    valor_2 = int(input('Digite o segundo valor inteiro: '))

    if valor_1 > valor_2:
        print(f'O primeiro valor {valor_1} é maior que o segundo valor {valor_2}.')

    elif valor_2 > valor_1:
        print(f'O segundo valor {valor_2} é maior que o primeiro valor {valor_1}.')

    else:
        print('Os dois valores são iguais.')

except:
    print('ERRO: Digite um valor válido. Ele precisa ser inteiro.')