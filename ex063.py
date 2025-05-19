#como eu fiz na primeira vez:

'''print('-' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 25)

limite = int(input('Digite quantos números você quer ver: '))
n1 = 0
n2 = 1

contador = 0

while contador < limite:

    if contador == 0:
        print(n1, end=' → ')
    elif contador == 1:
        print(n2, end=' → ')
    else:
        n3 = n2 + n1
        print(n3, end=' → ')
        n1 = n2
        n2 = n3
    contador += 1
print('FIM')'''


#Como poderia ter feito também:

print('-' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 25)

limite = int(input('Digite quantos números você quer ver: '))
n1 = 0
n2 = 1
print(n1, end=' → ')
print(n2, end=' → ')
contador = 3
while contador <= limite:
    n3 = n2 + n1
    print(n3, end=' → ')
    n1 = n2
    n2 = n3
    contador += 1
print('FIM')