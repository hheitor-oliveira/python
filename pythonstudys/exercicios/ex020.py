from random import sample
print('Exercício 020')
print('Qual será a ordem de apresentação dos grupos? ')
lista = 'Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4'
nova_lista = (sample(lista, k=4))
print(f'Após o sorteio a nova lista será: {nova_lista}')