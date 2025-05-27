tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Fluminense', 'Ceará', 'Bahia', 'Corinthians', 'Mirassol', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco da Gama', 'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport Recife')
print('-=' * 30)
print(f'Lista de times do Brasileirão 2025: {tabela}')
print('-=' * 30)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 30)
while True:
    time = input('Qual time você quer ver a posição na tabela? ')
    if time not in tabela:
        print('Digite corretamente o nome de um time da Série A do Brasileirão 2025.')
        print('-=' * 30)
    else:
        print(f'O {time} está na {tabela.index(time)+1}ª posição.')
        print('-=' * 30)