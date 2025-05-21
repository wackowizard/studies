#como eu fiz, somente com while
valor = 0
contador = 1
while valor >= 0:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-' * 30)
    while contador <= 10:
        print(f'{valor} x {contador} = {valor * contador}')
        contador += 1
    print('-' * 30)
    contador = 1
print('PROGRAMA TABUADA ENCERRADO. \nVolte sempre!')


#como também daria pra fazer, usando o while e for
'''while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for i in range(1, 11):
        print(f'{valor} X {i} = {valor * i}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. \nVolte sempre!')'''
