# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E ALTURA DE UMA PESSOA E CALCULE SEU IMG E MOSTRE SEUS STATUS.
# DE ACORDO COM A TABELA ABAIO
'''
ABAIXO DE 18.5: ABAIXO DO PESO
ENTRE 18.5 E 25: PESO IDEAL
DE 25 ATÉ 30: SOBREPESO
30 ATÉ 40: OBESIDADE
ACIMA DE 40: OBESIDADE MÓRBIDA
'''

print('=' * 20)
print('CALCULAR IMC')
print('=' * 20)

peso = float(input('Digite o seu peso KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO NORMAL, parabéns!')
elif imc >= 25 and imc <= 30:
    print('Você está ACIMA DO PESO ideal para a saúde!')
elif imc >= 30 and imc <= 40:
    print('Você está OBESO! SE CUIDE!!!')
else:
    print('Você está em estado de OBESIDADE MÓRBIDA!')
print(f'O seu IMC é de {imc:.2f}')