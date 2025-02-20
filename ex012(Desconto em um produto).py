p = float(input('Informe o preço do produto: R$'))
d = p - (p * 5/100)
print(f'O preço do produto é \033[32mR${p}\033[m \n'
      f'Com o desconto de 5% o valor passa a ser \033[34mR${d:.2f}\033[m')