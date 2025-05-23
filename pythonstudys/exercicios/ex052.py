# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

n1 = int(input('Digite um número inteiro ao lado: '))
tot = 0
for c in range(1, n1 +1):
    print(f'{c}', end=' ')
    if n1 % c == 0:
        tot += 1