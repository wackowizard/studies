numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número: '))
    if escolha < 0 or escolha > 20:
        print('Tente novamente. Escolha um número válido entre 0 e 20.')
    else:
        print(f'Você digitou o número {numeros[escolha]}.')

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        print('Encerrando o programa. Até logo!')
        break