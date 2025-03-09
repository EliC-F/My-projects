n = input('Digite o nome da sua cidade: ').strip()
print(f'O nome da sua cidade é {n.title()} \n'
      f'O nome da cidade começa com (Santo)? {'Santos' in n.title()}')
