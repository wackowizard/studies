limite = int(input('Digite um número: '))
n1 = 0
n2 = 1

contador = 0

while contador < limite:

    if contador == 0:
        print(n1)
    elif contador == 1:
        print(n2)
    else:
        n3 = n2 + n1
        print(n3)
        n1 = n2
        n2 = n3
    contador += 1
