r = float(input('Informe a quantidade de dinheiro que você possui: R$'))
print(f'A quantidade que você possui é de \033[32mR${r:.2f}\033[m \n'
      f'A quantidade de dolar que você pode comprar é de \033[34mUS${r / 5.16:.2f}\033[m \n'
      f'A quantidade de euro que você pode comprar é de \033[33m€{r / 5.37:.2f}\033[m')
