try:
    from datetime import date
    nascimento = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if idade == 18:
        print(f'Você tem {idade} anos e precisa se alistar este ano!')
    elif idade > 18:
        print(f'Você tem {idade} anos, então já deve ter se alistado há {idade - 18} anos atrás, em {ano_atual - (idade - 18)}!')
    else:
        print(f'Você tem {idade} anos, então faltam {18 - idade} anos para se alistar!')

except:
    print('ERRO: você precisa digitar um número válido.')