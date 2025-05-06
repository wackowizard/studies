salario = float(input('Digite o seu salário: R$'))

if salario >= 1200:
    print('Seu novo salário, com aumento de 10% é: R${:.2f}!'.format(salario * 1.10))

else:
    print('Seu novo salário, com aumento de 15% é: R${:.2f}!'.format(salario * 1.15))
