from random import randint

numero = randint(0, 10)

tentativas = 0
palpite = ''
while numero != palpite:
    palpite = int(input('Eu pensei em um número de 0 a 10. Tente adivinhar qual foi: '))
    if palpite > 10:
        print('Tente um número entre 0 e 10.')
    if numero != palpite:
        print(f'Não é {palpite}. Tente novamente! ')
        tentativas += 1
    if numero == palpite:
        tentativas += 1
if tentativas == 1:
    print(f'GÊNIO!!! Eu realmente tinha pensado em {numero}! Você precisou de apenas {tentativas} tentativa para acertar!!')
elif tentativas == 3:
    print(f'Parabéns, eu realmente tinha pensado em {numero}! Você precisou de apenas {tentativas} tentativas para acertar. Genial!')
elif tentativas < 6:
    print(f'Parabéns, eu realmente tinha pensado em {numero}! Você precisou de {tentativas} tentativas para acertar.')
else:
    print(f'Ok, eu realmente tinha pensado em {numero}, mas você precisou de {tentativas} tentativas para acertar. Deuzolivre...')
