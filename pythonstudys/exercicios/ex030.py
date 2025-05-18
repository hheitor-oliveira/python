#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR.

n1 = int(input('Digite um número: '))
if n1 % 2 == 0:
    print(f'O número {n1} é PAR!')
else:
    print(f'O número {n1} é IMPAR!')