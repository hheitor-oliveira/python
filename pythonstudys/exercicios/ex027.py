# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último ome separadamente.
# Ex: Ana Maria de Souza.
# Primeiro: Ana
# Ultímo: Souza
nome = str(input('Digite o seu nome completo: '))
nome = nome.capitalize().split()
print(f'Primeiro nome: {nome[0].capitalize()}')
print(f'Segundo nome: {nome[-1].capitalize()}')

