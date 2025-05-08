soma = 0
contador = 0
for i in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        contador += 1
        soma += numero
print(f'A soma dos {contador} números pares é {soma}')