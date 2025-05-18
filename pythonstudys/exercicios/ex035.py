# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA SE ELAS PODEM FORMAR UM TRIÂNGULO
# sorted organiza os números em ordem crescente

# PEGANDO OS VALORES
r1 = int(input('Digite o tamanho do segmento do triângulo: '))
r2 = int(input('Digite o tamanho do segmento do triângulo: '))
r3 = int(input('Digite o tamanho do segmento do triângulo: '))

#RESOLUÇÃO
if r1 < r2 + r3 and r2 < r1 + r3 and r1 < r3 + r2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triãngulo')