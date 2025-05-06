from random import choice, randint

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

nomes = [a1, a2, a3, a4]
r = choice(nomes)

index = randint(0 , len(nomes) - 1)
nomes_2 = nomes[index]

print('O aluno sorteado para apagar o quadro foi: {}'.format(r))
