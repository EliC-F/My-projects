n = input('Informe seu nome completo: ').strip().rstrip().title()
nl = n.split()
print(f'O seu nome completo é {n} \n'
      f'O seu primeiro nome é {nl[0]} \n'
      f'O seu ultimo nome é {nl[-1]}')
