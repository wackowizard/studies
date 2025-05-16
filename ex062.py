print('GERADOR DE PA')
print('-' * 20)

numero = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termos = 10
total = 0
pa = numero

while termos != 0:
    contador = 0
    while contador < termos:
        print(f'{pa}', end=' → ')
        pa += razao
        contador += 1
        total += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer ver a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')