numero = int(input('Digite um número inteiro: '))

for asterisco in range(numero, 0, -1):
    espacos = numero - asterisco

    linha = ' ' * espacos + '*' * asterisco
    print(linha)

# espaco = ''
# for linha in range(numero, 0, -1):
#     asterisco = ''
#     for coluna in range(0, linha, 1):
#         asterisco = asterisco + '*'
#     print(espaco + asterisco)
#     espaco = espaco + ' '
