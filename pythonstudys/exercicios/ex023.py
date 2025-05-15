# Faça um programa que leia um número de 0 a 9999  e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

n1 = input('Digite um número de 0 a 9999: ')
if n1.isnumeric():
    lista_numero = n1.zfill(4)
    print(lista_numero)