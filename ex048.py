soma = 0
contador = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        contador += 1
print(f'Ao todo são {contador} números ímpares e múltiplos de 3 entre 1 e 500. E a soma deles é {soma}')
