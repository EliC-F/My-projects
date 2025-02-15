n = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n + n2) / 2
if m >= 7:
    print(f'A primeira nota do aluno foi \033[1;36m{n}\033[m \n'
          f'A segunda nota do aluno foi \033[1;36m{n2}\033[m \n'
          f'A media do aluno é \033[1;34m{m}\033[m')
else:
    print(f'A primeira nota do aluno foi \033[1;36m{n}\033[m \n'
          f'A segunda nota do aluno foi \033[1;36m{n2}\033[m \n'
          f'A media do aluno é \033[1;31m{m}\033[m')
