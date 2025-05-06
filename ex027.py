name = str(input('Digite um nome completo: ')).strip()
first_name = name.split()[0]
last_name = name.split()[-1]
print('Se o seu nome é {}, então seu primeiro nome é {} e seu último nome é {}'.format(name, first_name, last_name))
