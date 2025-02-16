print('CONVERSOR DE MEDIDAS')
print('\033[1;36m-=\033[m' * 25)
m = float(input('Digite o valor em metros: '))
print(f'O valor em metros é igual a \033[32m{m}\033[m \n'
      f'Quilometro: \033[35m{m / 1000}\033[mkm. \n'
      f'Hectometro: \033[34m{m / 100}\033[mhm. \n'
      f'-Decametro: \033[32m{m / 10}\033[mdam. \n'
      f'-    Metro: \033[32m{m}\033[mm \n'
      f'-Decimetro: \033[33m{m * 10}\033[mdm. \n'
      f'Centimetro: \033[34m{m * 100}\033[mcm. \n'
      f'-Milimetro: \033[35m{m * 1000}\033[mmm.')
print('\033[1;36m-=\033[m' * 25)
