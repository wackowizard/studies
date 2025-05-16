numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
pa = numero
contador = 10

while contador > 0:
    print(f'{pa}')
    pa += razao
    contador -= 1
