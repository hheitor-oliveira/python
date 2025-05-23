# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA P.A, NO FINAL MOSTRE
# OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

t1 = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
decimo = t1 + (10 - 1) * razão
for c in range(t1, decimo + razão, razão):
    print(f'{c}', end=' - ')