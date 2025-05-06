numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

#como eu fiz, sem usar condicionais
'''maior = max(numero_1, numero_2, numero_3)
menor = min(numero_1, numero_2, numero_3)'''

#como poderia ter feito também
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

print('O maior número é o {} e o menor é o {}.'.format(maior, menor))

