reta_1 = float(input('Digite o primeiro complimento de reta: '))
reta_2 = float(input('Digite o segundo comprimento de reta: '))
reta_3 = float(input('Digite o terceiro comprimento de reta: '))

if (reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_2 + reta_3) > reta_1:
    print('É possível formar um triêngulo!')

else:
    print('Não é possível formar um triângulo...')