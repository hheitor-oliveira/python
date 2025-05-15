# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

nome = str(input('Digite seu nome: '))
nome = nome.upper()
print(f'A letra "A" aparece {nome.count('A')} vezes no seu nome.')
print(f'A letra "A" aparece pela primeira vez na posição {nome.find('A')}')
print(f'A letra "A" aparece pela última vez na posição {nome.rfind('A')}')