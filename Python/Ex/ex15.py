dias = int(input('Quantos dias você utilizou o carro? '))
km = float(input('Quantos Km você percorreu? '))
total = (dias * 60) + (km * 0.15)

print(f'O valor total do aluguel é de R$ {total}')