nu = int(input('Digite um numero de 0 a 9999: '))
n = f'{nu:04d}'
u = n[3]
d = n[2]
c = n[1]
um = n[0]
print(f'O numero digitado foi {nu} e ele: \n'
      f'Tem {u} unidades \n'
      f'Tem {d} dezenas \n'
      f'Tem {c} centenas \n'
      f'Tem {um} unidades de milhar')
print('\n')
num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O numero digitado foi {num} \n'
      f'unidade: {u} \n'
      f'dezena: {d} \n'
      f'centena: {c} \n'
      f'Milhar: {m}')