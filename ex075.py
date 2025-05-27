#como fiz na segunda
numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')


#como eu fiz na primeira vez
'''numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))
numero_4 = int(input('Digite o último número: '))
numeros = (numero_1, numero_2, numero_3, numero_4)

nove = 0
pares = 0

for valor in numeros:
    if valor == 9:
        nove += 1
    if valor % 2 == 0:
        pares += 1

print(f'Você digitou os valores {numeros}')

if nove == 0:
    print('O valor 9 não apareceu nenhuma vez.')
else:
    print(f'O valor 9 apareceu {nove} vezes.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu nenhuma vez.')

print(f'Você digitou {pares} números pares!')'''