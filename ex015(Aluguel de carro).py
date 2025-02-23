k = float(input('Informe a quantidade de Quilometros percorrido: '))
d = int(input('Informe a quantidade de Dias que o carro foi alugado: '))
ck = 0.15 * k
cd = 60 * d
print(f'A quantidade de Quilometros foi de \033[31m{k:.2f}km\033[m e de dias foi de \033[34m{d} dias\033[m \n'
      f'A quantidade total a se pagar é igual \033[32mR${ck + cd:.2f}\033[m')
