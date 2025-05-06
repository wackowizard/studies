n = float(input('Digite o valor atual do salário: R$'))
a = n * 1.15
d = a - n
print('Com o aumento de 15%, o novo valor do salário fica R${:.2f}! Ou seja, um acréscimo de R${:.2f}.'.format(a, d))
