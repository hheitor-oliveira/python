# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.upper()
print('SANTO' in cidade)
print('Se retornado False, não há "SANTO" na codade digitada.\nSe True, há sim.')