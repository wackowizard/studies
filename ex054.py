from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for i in range(0, 7, 1):
    data = int(input('Digite seu ano de nascimento: '))
    idade = (ano_atual - data)

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'São {maiores} maiores de idade e {menores} menores de idade')
