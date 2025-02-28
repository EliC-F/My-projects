from random import shuffle

a1 = input('Informe o nome: ')
a2 = input('Informe o nome: ')
a3 = input('Informe o nome: ')
a4 = input('Informe o nome: ')
o = [a1, a2, a3, a4]

shuffle(o)

print(f'A ordem sorteada foi {o}')
