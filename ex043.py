try:
    #Receber os dados
    altura = float(input('Digite sua altura, em metros (exemplo: 1.82): '))
    peso = float(input('Digite seu peso, em kg (exemplo: 76): '))

    #Calcurar o IMC
    imc = peso / (altura ** 2)
    print(f'Seu IMC é {imc:.1f}')

    #Comparar com a tabela e gerar uma resposta
    if imc <= 18.5:
       print('Então você está ABAIXO DO PESO.')
    elif imc > 18.5 and imc <= 25:
        print('Então você está no PESO IDEAL.')
    elif imc > 25 and imc <= 30:
        print('Então você está com SOBREPESO.')
    elif imc > 30 and imc <= 40:
        print('Então você está com OBESIDADE.')
    else:
        print('Então você está com OBESIDADE MÓRBIDA.')
except:
    print('ERRO: Digite apenas números.')