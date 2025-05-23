# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
# SE O VALOR DIGITADO FOR ÍMPAR DESCONSIDERE-O.
soma = 0
cont = 0
lista_impar = []
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
    elif n % 2 >= 1:
        lista_impar.append(n)

print(f'A soma de {cont} valores PARES e resultou em {soma}')
print(f'Os valores desconsiderados foram {lista_impar}')