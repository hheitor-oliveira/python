#from math import sqrt, factorial, ceil, floor (AQUI ESTOU SELECIONANDO FUNCIONALIDADES ESPECÍFICAS)
#import math (AQUI ESTOU IMPORTANDO A BIBLIOTECA INTEIRA, E NÃO SELECIONANDO NADA ESPECÍFICO)

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')