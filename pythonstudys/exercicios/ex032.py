# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

n1 = int(input('Digite um ano, para verificar se ele é bissexto: '))

if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print(f'O ano de {n1} é um ano bissexto.')
else:
    print(f'Não, {n1} não é um ano bissexto.')