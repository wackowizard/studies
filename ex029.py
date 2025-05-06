velocidade = float(input('A velocidade do carro, em km/h: '))

if velocidade > 80:
    print('Você foi multado! O limite de velocidade nesta via é de 80km/h.')
    print('E o valor da sua multa é R${:.2f}.'.format((velocidade - 80) * 7))
else:
    print('Você está dentro da velocidade permitida.')
