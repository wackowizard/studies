from random import randint

computador = randint(0, 10)

print('-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 30)

contador = vitorias = derrotas = 0

while derrotas == 0:
    valor = int(input('Digite um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    contador += 1
    soma = valor + computador
    if soma % 2 == 0 and jogador == 'P':
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {soma}, deu par.')
        print('Você venceu!')
        vitorias += 1
    elif soma % 2 == 0 and jogador != 'P':
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {soma}, deu par.')
        print('Você perdeu!')
        derrotas += 1
    elif soma % 2 != 0 and jogador == 'P':
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {soma}, deu ímpar.')
        print('Você perdeu!')
        derrotas += 1
    elif soma % 2 != 0 and jogador != 'P':
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {soma}, deu ímpar.')
        print('Você venceu!')
        vitorias += 1
print('-' * 30)
print(f'GAME OVER! Você venceu {vitorias} vezes.')