from math import hypot

o = float(input('Informe o comprimento do cateto oposto: '))
a = float(input('Informe o comprinto do cateto adjacente: '))
h = hypot(o, a)
print(f'O cateto oposto é igual a {o:.2f} \n'
      f'O cateto adjacente é igual a {a:.2f} \n'
      f'A hipotenusa tem o resultado igual {h:.2f}.')
# Outra forma de Fazer:
#o = float(input('Digite o valor do cateto oposto: '))
#a = float(input('Digite o valor do cateto adjacente: '))
#h = (o ** 2 + a ** 2) ** (1/2)
#print(f'O cateto o. vale {o:.2f} \n'
      #f'O cateto a. vael {a:.2f} \n'
      #f'A h. tem o resutado igual a {h:.2f}')