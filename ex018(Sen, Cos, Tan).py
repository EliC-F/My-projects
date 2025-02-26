from math import sin, cos, tan, radians

a = float(input('informe o valor do angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O angulo informado foi {a} \n'
      f'O seu seno vale {s:.2f} \n'
      f'O seu cosseno vale {c:.2f} \n'
      f'A sua tangente vale {t:.2f}')
