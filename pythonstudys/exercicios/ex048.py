# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS
# E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

for n in range(0, 500):
    impar = n % 2
    multiplo = n % 3
    if impar >= 1 and multiplo == 0:
