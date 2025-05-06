try:
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    media = (nota_1 + nota_2) / 2

    if media < 5:
        print(f'A média das notas {nota_1} e {nota_2} é {media}. Então você está reprovado!')

    elif media > 5 and media < 6.9:
        print(f'A média das notas {nota_1} e {nota_2} é {media}. Então você está em recuperação!')

    else:
        print(f'A média das notas {nota_1} e {nota_2} é {media}. Enão você está aprovado!')
except:
    print('ERRO: insira um número válido.')