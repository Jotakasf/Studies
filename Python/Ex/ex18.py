import math
a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O ângulo {a} possui \nSeno: {s:.2f} \nCosseno: {c:.2f} \nTangente: {t:.2f}')