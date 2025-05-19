resposta = 'S'
soma = quantidade = media = maior = menor = 0 #quando mais de uma variável recebe o mesmo valor, é possível estruturá-las na mesma linha

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')










'''numero = 0
maior = 0
menor = 5000
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um valor (999 para parar): '))
    soma += numero
    contador += 1
    if numero > maior and numero != 999:
        maior = numero
    elif numero < menor:
        menor = numero
media = (soma - 999) / (contador - 1)

print(f'O maior número digitado foi {maior} e o menor foi {menor}. E a média é de {media}')'''