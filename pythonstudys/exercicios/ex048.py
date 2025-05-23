# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS
# E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

lista = []
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        lista.append(n)
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {sum(lista)}')