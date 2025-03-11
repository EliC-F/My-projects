f = input('Digite algo: ').strip().rstrip().upper()
print(f'A letra (A) apareceu {(f.count('A'))} vezes \n'
      f'A primeira vez que (A) apareceu foi na posição {f.find('A') + 1} \n'
      f'A ultima vez em que (A) apareceu foi na posição {f.rfind('A') + 1} ')
