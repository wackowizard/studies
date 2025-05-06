try:
    valor = int(input('Digite um número inteiro: '))
    tipo_conversão = int(input('Para converter este número, digite: \n 1 para binário \n 2 para octal \n 3 para hexadecimal \n Escolha: '))

    if tipo_conversão == 1:
        binário = bin(valor)[2:]
        print(f'O valor {valor}, em binário é {binário}')

    elif tipo_conversão == 2:
        octal = oct(valor)[2:]
        print(f'O valor {valor}, em octal é {octal}')

    elif tipo_conversão == 3:
        hexadecimal = hex(valor)[2:]
        print(f'O valor {valor}, em hexadecimal é {hexadecimal}')

    else:
        print(f'A opção não é compatível.')

except ValueError:
    print('Você precisa digitar um número inteiro válido.')