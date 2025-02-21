s = float(input('Informe o salario do funcionario: R$ '))
ns = s + (s * 15 / 100)
print(f'O salario do funcionario é igual a \033[31mR${s:.2f}\033[m \n'
      f'Com o aumento de 15% passa a ser \033[34mR${ns:.2f}\033[m')
