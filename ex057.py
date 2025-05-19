sexo = ''
while sexo == 'M' or 'F':
    sexo = input('Digite seu sexo (F ou M): ').upper().strip()
    if sexo == 'M':
        print(f'Legal, seu sexo é masculino\n')
    elif sexo == 'F':
        print(f'Legal, seu sexo é feminino\n')
    else:
        print('Preciso de um valor válido...\n')
