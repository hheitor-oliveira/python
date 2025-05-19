# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM:
# - O PRIMEIRO VALOR É MAIOR.
# - O SEGUNDO VALOR É MAIOR
# - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'O Primeiro valor é maior. {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O Segundo valor é maior. {n2} é maior que {n1}')
elif n1 == n2:
    print('Não existe valor maior, os dois valores são iguais.')