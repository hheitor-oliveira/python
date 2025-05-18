# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2 ,n3)
print(f'O maior número digitado é {maior}')
print(f'O menor número digitado é {menor}')