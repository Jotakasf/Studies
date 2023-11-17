import random
a1 = str(input('Primeiro membro: '))
a2 = str(input('Segundo membro: '))
a3 = str(input('Terceiro membro: '))
a4 = str(input('Quarto membro: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)