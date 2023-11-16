from math import sqrt, pow
cao = float(input('Qual o comprimento do cateto oposto? '))
caa = float(input('Qual o comprimento do cateto adjacente? '))
h = sqrt(pow(cao, 2) + pow(caa, 2))
print(h)