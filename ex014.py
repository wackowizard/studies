km = float(input('Digite quantos quilômetros percorreu: '))
d = int(input('Digite quantos dias esteve com o carro: '))
preço_dia = d * 60
preço_km = km * 0.15
custo = preço_km + preço_dia
print('Com {}km rodados em {:.0f} dias de aluguel, o valor fica R${:.2f}.'.format(km, d, custo))
