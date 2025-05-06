from datetime import date
try:
    nascimento = int(input('Digite seu ano de nascimento para saber qual sua categoria na natação: '))
    data = date.today().year
    idade = data - nascimento
    if idade <= 9:
        print(f'Você tem {idade} anos, então faz parte da categoria MIRIM!')
    elif idade > 9 and idade <= 14:
        print(f'Você tem {idade} anos, então faz parte da categoria INFANTIL!')
    elif idade > 14 and idade <= 19:
        print(f'Você tem {idade} anos, então faz parte da categoria JÚNIOR!')
    elif idade == 20:
        print(f'Você tem {idade} anos, então faz parte da categoria SÊNIOR!')
    else:
        print(f'Você tem {idade} anos, então faz parte da categoria MASTER!')
except:
    print('ERRO: Digite um valor válido. Exemplo: 1997')