n = float(input('Digite um numero: '))
print(f'O numero digitado é o \033[37m{n}\033[m \n'
      f'O seu dobro vale \033[31m{n * 2}\033[m \n'
      f'O seu triplo vale \033[33m{n * 3}\033[m \n'
      f'A sua raiz quadrada vale \033[34m{n ** (1 / 2):.2f}\033[m')