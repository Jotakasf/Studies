n = str(input('Digite o seu nome completo: '))
print(n.upper())
print(n.lower())
d = n.split()
print(f"Seu nome possui {len(''.join(d))} letras")
print(f"Seu primeiro nome é {d[0]} e ele possui {len(d[0])} letras")

