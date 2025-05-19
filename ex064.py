numero = 0
total = 0
contador = 0
numero = int(input('Digite um número (999 para parar): ')) #Duplicar o comando para o flag não for somado e não precisar colocar 'soma - 999' ou 'contador - 1'
while numero != 999:
    total += numero
    contador += 1
    numero = int(input('Digite um número (999 para parar): '))
print(f'Você digitou {contador} números. E a soma deles vale: {total}')