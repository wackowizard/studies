#com string
'''num = str(input('Digite um número de 0 a 9999: '))
unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))'''

#com math
num = int(input('Digite um número de 0 a 9999: '))
num_digitos = f'{num:04}'

if num >= 10000:
    print('O número {} é inválido, pois precisa ser menor do que 9999. Tente novamente!'. format(num))

else:
    print('M ilhar: ', num_digitos[0])
    print('Centena: ', num_digitos[1])
    print('Dezena: ', num_digitos[2])
    print('Unidade: ', num_digitos[3])

#resolução curso
'''num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))'''