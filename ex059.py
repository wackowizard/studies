opcao = ''
while opcao != 0:
    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número: '))

    print('[1] somar\n[2] multiplicar\n[3] dividir\n[4] maior\n[5] novos números\n[0] sair do programa')
    opcao = int(input('>>>> Digite a opção escolhida: '))

    if opcao == 1:
        print(f'{numero_1:.0f} + {numero_2:.0f} = {numero_1 + numero_2:.0f}\n')

    elif opcao == 2:
        print(f'{numero_1:.0f} x {numero_2:.0f} = {numero_1 * numero_2:}\n')

    elif opcao == 3:
        print(f'{numero_1:.0f} / {numero_2:.0f} = {numero_1 / numero_2:.0f}\n')

    elif opcao == 4:
        if numero_1 > numero_2:
            print(f'O número {numero_1:.0f} é maior que o número {numero_2:.0f}.\n')
        elif numero_1 == numero_2:
            print('Os números são iguais.\n')
        else:
            print(f'O número {numero_2:.0f} é maior que o número {numero_1:.0f}\n')

    elif opcao == 5:
        print('\nOk, escolha novos valores: \n')

    elif opcao > 5 or opcao < 0:
        print('Tente uma opção válida...\n')

print('Calculadora encerrada. Obrigado por usar!')
