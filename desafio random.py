# Função para formatar valores em reais com separadores de milhar no estilo brasileiro (com ajuda do GPT)
def formatar_reais(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

# Coletar os dados
dias_simulacao = int(input('Digite o número de dias que você quer simular: '))
escolha = int(input('[1] = R$ 1 bilhão por dia\n[2] = R$ 0,1 centavo, mas o valor dobra todo dia\nEscolha: '))

# Cálculo escolha 1
escolha_1 = dias_simulacao * 1_000_000_000

# Cálculo escolha 2
dinheiro = 0.001  # 0,1 centavo em reais
acumulado = dinheiro
valores_diarios_1 = [1_000_000_000 * (i + 1) for i in range(dias_simulacao)]
valores_diarios_2 = [acumulado]

for _ in range(1, dias_simulacao):
    dinheiro *= 2
    acumulado += dinheiro
    valores_diarios_2.append(acumulado)

escolha_2 = acumulado

# Verificar quando a opção 2 passa a superar a 1 (em até 100 dias)
dinheiro_extra = 0.001
acumulado_extra = dinheiro_extra
dia_supera = None
for i in range(1, 100):
    dinheiro_extra *= 2
    acumulado_extra += dinheiro_extra
    if acumulado_extra > (1_000_000_000 * (i + 1)):
        dia_supera = i + 1
        break

# Exibir resultados
print()
if escolha == 1:
    print(f'Em {dias_simulacao} dias, você teria: {formatar_reais(escolha_1)}.')
elif escolha == 2:
    print(f'Em {dias_simulacao} dias, você teria: {formatar_reais(escolha_2)}.')
else:
    print('Digite uma opção válida (1 ou 2).')

# Comparação final
if escolha_2 > escolha_1:
    diferenca = escolha_2 - escolha_1
    print(f'Nessa quantidade de dias, a escolha 2 daria {formatar_reais(diferenca)} a mais que a escolha 1.')
else:
    diferenca = escolha_1 - escolha_2
    print(f'Nessa quantidade de dias, a escolha 1 daria {formatar_reais(diferenca)} a mais que a escolha 2.')

# Mostrar o ponto de virada
if dia_supera:
    print(f'A escolha 2 passa a ser mais vantajosa a partir do dia {dia_supera}.')