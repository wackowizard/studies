numero = int(input('Digite um número inteiro e veja se ele é primo: '))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'\033[32m{i}\033[m', end=' ')  # Verde para divisores
        contador += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')  # Vermelho para não divisores

print(f'\n\nO número {numero} foi divisível {contador} vezes.')

if contador == 2:
    print('Então é primo!')
else:
    print('Então não é primo!')
