#Como eu fiz de primeira
'''nome = str(input('Digite um nome: ')).strip()
silva = nome.find('Silva')
if silva <= -1:
    print('O nome não tem "Silva"!')

else:
    print('O nome tem "Silva"!"')'''

#nova tentativa
nome = str(input('Digite um nome: ')).strip()
silva = 'silva' in nome.lower()

if silva is True:
    print('O nome tem Silva!')

else:
    print('O nome não tem Silva.')