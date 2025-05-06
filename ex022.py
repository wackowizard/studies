nome = str(input('Digite seu nome completo: ')).strip()
print('Já que seu nome é {}, então:'.format(nome))
print('Seu nome completo em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome completo em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras, sem contar espaços'.format(len(nome) - nome.count(' ')))
n_first = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(n_first[0], len(n_first[0])))



