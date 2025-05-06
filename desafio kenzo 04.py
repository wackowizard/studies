numero = int(input('Digite um número inteiro: '))

for asterisco in range (1, numero + 1, + 1):
    espaco = numero - asterisco

    linha = ' ' * espaco + '*' * asterisco
    print(linha)