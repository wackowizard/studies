numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
décimo = numero + (10 - 1) * razao
for i in range (numero, décimo + razao, razao):
    print(i, end= ' ➜ ')
print('ACABOU!')