from random import randint
from time import sleep
escolha = randint(0, 5)
palpite = int(input('Pensei em um número de 0 a 5. Digite qual você acha que eu pensei: '))

print('E você...') #Só para dar um suspense
sleep(2)

if palpite == escolha:
    print('Acertou! Parabéns, realmente foi esse número!')
else:
    print('Errou! Eu havia pensado em: {}'.format(escolha))
