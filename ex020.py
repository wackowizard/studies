from random import shuffle
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
nomes = [a1, a2, a3, a4]
shuffle(nomes)
print('A ordem de apresentação dos alunos é: ')
print(nomes)