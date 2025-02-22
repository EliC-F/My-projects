c = float(input('Informe a temperatura em graus celsius(°C): '))
f = (c * 1.8) + 32
k = c + 273.15
if c >= 30:
    print(f'A temperatura em graus celsius(°C) informada é de: \033[31m{c:.2f}°C\033[m \n'
          f'Convertendo para Fahrenheit(F) é igual a: \033[35m{f:.2f}°F\033[m \n'
          f'Convertendo para Kelvin(K) é igual a: \033[33m{k:.2f}°K\033[m')
else:
    print(f'A temperatura em graus celsius(°C) informada é de: \033[34m{c:.2f}°C\033[m \n'
          f'Convertendo para Fahrenheit(F) é igual a: \033[37m{f:.2f}°F\033[m \n'
          f'Convertendo para Kelvin(K) é igual a: \033[32m{k:.2f}°K\033[m')
