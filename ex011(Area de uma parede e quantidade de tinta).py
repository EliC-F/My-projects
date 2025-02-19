l = float(input('Informe a larhura da parede em metros: '))
al = float(input('Infrome a altura da parede em metros: '))
print(f'Sua parede tem a dimensão igual a \033[1m{l}m x {al}m\033[m \n'
      f'Sua area é igual a \033[34m{l * al}m²\033[m \n'
      f'A quantidade de tinta nescessaria para pintar a parede é de \033[36m{l * al / 2}l\033[m')
