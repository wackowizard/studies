print('=' * 30)
print('{:^30}'.format('BANCO ELETRÔNICO'))
print('=' * 30)

cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0
valor = 0

while True:
    valor = int(input('Que valor você quer sacar? R$ '))

    while (valor - 50) >= 0:
        cedula_50 += 1
        valor -= 50

    while (valor - 20) >= 0:
        cedula_20 += 1
        valor -= 20

    while (valor - 10) >= 0:
        cedula_10 += 1
        valor -= 10

    while (valor - 1) >= 0:
        cedula_1 += 1
        valor -= 1
    break

if cedula_50 > 0:
    print(f'Total de {cedula_50} cédulas de R$50')
if cedula_20 > 0:
    print(f'Total de {cedula_20} cédulas de R$20')
if cedula_10 > 0:
    print(f'Total de {cedula_10} cédulas de R$10')
if cedula_1 > 0:
    print(f'Total de {cedula_1} cédulas de R$1')


#uma outra forma (e provavelmente melhor) de fazer
'''print('=' * 30)
print('{:^30}'.format('BANCO ELETRÔNICO'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))

for cedula in [50, 20, 10, 1]:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R${cedula}')'''