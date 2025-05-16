#com for
'''numero = int(input('Digite um número para saber seu fatorial: '))
fatorial = numero
for i in range (numero - 1, 0, -1):
    fatorial *= i
print(f'O fatorial de {numero} é: {fatorial}'''

#com while
numero = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'O fatorial de {numero} é: {fatorial}')
