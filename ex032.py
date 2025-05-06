from datetime import date #Pegar a data atual da máquina
ano = int(input('Digite um ano para analisar. (coloque 0 para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))

else:
    print('O ano {} não é bissexto!'.format(ano))
