cidade = str(input('Digite o nome de uma cidade: ')).strip()
santo = (cidade[:5].upper() == 'SANTO')

if santo is True:
    print('A cidade começa com "Santo"!')

else:
    print('A cidade não começa com "Santo"')


