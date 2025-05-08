frase = input('Digite uma frase para ver se é palíndromo: ').lower().replace(' ', '')
invertido = ''
for i in range(len(frase) -1, -1, -1):
    invertido += frase[i]
if frase == invertido:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')


#Como fiz primeiro, só com condicionais
'''frase = input('Digite uma frase para ver se é palíndromo: ').lower().replace(' ', '')
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')'''