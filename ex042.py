try:

    reta_1 = float(input('Digite o primeiro valor: '))
    reta_2 = float(input('Digite o segundo valor: '))
    reta_3 = float(input('Digite o terceiro valor: '))

    if (reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_2 + reta_3) > reta_1:
        print('É possível fazer um triângulo!')
        if reta_1 == reta_2 == reta_3:
            print('E este triângulo é um equilátero, pois todos os lados são iguais')
        elif (reta_1 == reta_2 != reta_3) or (reta_1 == reta_3 != reta_2) or (reta_2 == reta_3 != reta_1):
            print('E este triângulo é isósceles, pois somente dois lados são iguais')
        elif (reta_1 != reta_2) and (reta_1 != reta_3) and (reta_2 != reta_3):
            print('E este triângulo é escaleno, pois todos os lados são diferentes!')

    else:
        print('Não é possível fazer um triângulo!')

except:
    print('ERRO: Insira um valor válido.')
