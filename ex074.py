#como eu poderia ter feito
from random import randint
escolha = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {escolha}')
print(f'O maior valor sorteado foi {max(escolha)}')
print(f'O menor valor sorteado foi {min(escolha)}')


#como eu fiz na segunda vez
'''from random import randint

escolha = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {escolha}')

maior = menor = escolha[0]

for valor in escolha:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''


#como eu fiz na primeira vez
'''from random import randint
escolha = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {escolha}')

maior = menor = contador = 0

for i in range(0, 5):
    if i == 0:
        maior = escolha[0]
        menor = escolha[0]
        contador += 1
    elif i >= 1:
        if escolha[i] > maior:
            maior = escolha[i]
        if escolha[i] < menor:
            menor = escolha[i]

print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''