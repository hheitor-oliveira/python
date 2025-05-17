# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: '))
print('Analisando seu nome...')
print(f'O nome escrito apenas em letras maiúsculas é: {nome.upper()}')
print(f'O nome escrito apenas em letras minúsculas é: {nome.lower()}')
nospace = nome.replace(' ', '')
print(f'A quantidade de caracteres que seu nome tem é: {len(nospace)}')
lista = nome.split()
print(f'Seu primeiro nome tem {len(lista[0])} caracteres.')
