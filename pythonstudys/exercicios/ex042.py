# REFAÇA O DESAFIO 35 DOS TRIÂNGULOS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIP ODE TRIÂNGULO SERÁ FORMADO:

# PEGANDO OS VALORES
r1 = int(input('Digite o tamanho do segmento do triângulo: '))
r2 = int(input('Digite o tamanho do segmento do triângulo: '))
r3 = int(input('Digite o tamanho do segmento do triângulo: '))

#RESOLUÇÃO
if r1 < r2 + r3 and r2 < r1 + r3 and r1 < r3 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO!')
    if r1 == r2 != r3 != r1 or r1 == r3 != r2 != r1 or r2 == r3 != r1 != r2:
        print('ISÓSCELES!')
else:
    print('Os segmentos não podem formar um triãngulo')
