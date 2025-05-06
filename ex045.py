from random import choice
from time import sleep
opções = ['pedra', 'papel', 'tesoura']
vitórias = 0
derrotas = 0
empates = 0

while True:
    jogador = str(input('Escolha pedra, papel ou tesoura ("sair" para ver o placar): ')).lower()

    if jogador == 'sair':
        print('\n---PLACAR FINAL---')
        print(f'Vitórias: {vitórias}')
        print(f'Derrotas: {derrotas}')
        print(f'Empates: {empates}')
        if vitórias != 0 or derrotas != 0 or empates != 0:
            print('~ Obrigado por jogar!')
        else:
            print(' ~ Ué, mas você nem tentou jogar, seu safado!')
        break

    if jogador not in opções:
        print('Escolha inválida. Tente novamente')
        continue

    computador = choice(opções)

    print('='*12)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('=' * 12)

    if jogador == computador:
        print(f'EMPATE! Você escolheu {jogador} e eu também escolhi {computador}.\n')
        empates += 1
    elif jogador == 'pedra' and computador == 'papel':
        print(f'PERDEU! Eu escolhi PAPEL e ele vence de PEDRA.\n')
        derrotas += 1
    elif jogador == 'pedra' and computador == 'tesoura':
        print(f'VENCEU! Eu escolhi TESOURA e ela perde para sua PEDRA.\n')
        vitórias += 1
    elif jogador == 'papel' and computador == 'tesoura':
        print(f'PERDEU! Eu escolhi TESOURA e ele vence seu PAPEL.\n')
        derrotas += 1
    elif jogador == 'papel' and computador == 'pedra':
        print(f'VENCEU! Eu escolhi PEDRA e ela perde para seu PAPEL.\n')
        vitórias += 1
    elif jogador == 'tesoura' and computador == 'pedra':
        print(f'PERDEU! Eu escolhi PEDRA e ela vence sua TESOURA.\n')
        derrotas += 1
    elif jogador == 'tesoura' and computador == 'papel':
        print(f'VENCEU! Eu escolhi PAPEL e ele perde para sua TESOURA.\n')
        vitórias += 1
