# Crie um programa que leia o nome de uma pessoa e diga se ele tem "SILVA" no nome.

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o seu nome: ').strip()
cidade = cidade.upper()
print('SILVA' in cidade)
print('Se retornado False, não há "SANTO" na codade digitada.\nSe True, há sim.')