import random

a1 = input('Informe o primeiro nome: ')
a2 = input('Informe o segundo nome: ')
a3 = input('Infrome o terceiro nome: ')
a4 = input('Informe o quarto nome: ')
s = random.choice([a1,a2,a3,a4])
print(f'O nome sorteado foi: {s}')