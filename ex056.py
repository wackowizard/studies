soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f'--------- PESSOA {i} ---------')
    nome = input(f'Digite o nome da {i}ª pessoa: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    if sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1

if nome_homem_mais_velho:
    print(f'O nome do homem mais velho é {nome_homem_mais_velho}, com {maior_idade_homem} anos de idade')
else:
    print('Não há homens no grupo')

media_idade = soma_idade / 4

print(f'A média de idade do grupo é {media_idade}')

print(f'E o número de mulheres com menos de 20 anos é: {mulheres_menos_20}.')
