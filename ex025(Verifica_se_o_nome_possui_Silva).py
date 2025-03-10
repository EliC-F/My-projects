n = input('Informe seu nome completo: ').strip()
print(f'O seu nome é {n.title()} \n'
      f'O seu nome possui Silva? {'Silva' in n.title()}')
