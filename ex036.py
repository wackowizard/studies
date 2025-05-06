valor_casa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do seu salário, em reais: R$'))
anos = int(input('Digite em quantos anos você pretende pagar: '))

parcelas_mes = anos * 12
valor_mes = valor_casa / parcelas_mes

if valor_mes > (salario * 0.30):
    print('Você não pode fazer este empréstimo, pois serão {:.0f} parcelas de R${:.2f}. Isso é superior a 30% do seu salário.'.format(parcelas_mes, valor_mes))
else:
    print('Perfeito! Você pode financiar essa casa em {:.0f} parcelas de R${:.2f}!'.format(parcelas_mes, valor_mes))

