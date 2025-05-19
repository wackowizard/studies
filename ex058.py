from random import randint

numero = randint(0, 10)

tentativas = 0
palpite = ''
print('Eu pensei em um número de 0 a 10.')
while numero != palpite:
    palpite = int(input('Tente adivinhar qual foi: '))
    if palpite > 10:
        print('Tente um número entre 0 e 10.')
    elif numero != palpite:
        if palpite > numero:
            print(f'Não é {palpite}, é menos... Tente novamente! ')
        else:
            print(f'Não é {palpite}, é mais... Tente novamente! ')
        tentativas += 1
    elif numero == palpite:
        tentativas += 1

if tentativas == 1:
    print(f'GÊNIO!!! Eu realmente tinha pensado em {numero}! Você precisou de apenas {tentativas} tentativa para acertar!!')
elif tentativas == 3:
    print(f'Parabéns, eu realmente tinha pensado em {numero}! Você precisou de apenas {tentativas} tentativas para acertar. Genial!')
elif tentativas < 6:
    print(f'Parabéns, eu realmente tinha pensado em {numero}! Você precisou de {tentativas} tentativas para acertar.')
else:
    print(f'Ok, eu realmente tinha pensado em {numero}, mas você precisou de {tentativas} tentativas para acertar. Deuzolivre...')
