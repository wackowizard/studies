print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)

mais_18 = homens = mulheres_menos_20 = 0

while True:
    while True:
        idade_str = input('Idade: ').strip()
        if idade_str.isdigit():
            idade = int(idade_str)
            break
        else:
            print('Idade inválida! Digite um número inteiro positivo.')

    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            break
        else:
            print('Sexo inválido! Digite apenas M ou F.')

    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    print('-' * 20)

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Opção inválida! Digite apenas S ou N.')

    if continuar == 'N':
        break

print('=' * 30)
print(f'Total de pessoas com mais de 18 anos: {mais_18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos.')
