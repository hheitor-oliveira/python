# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1.250.00 CALCULE UM AUMENTO DE 10%
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = float(input('Qual é o seu salário atualmente na empresa? '))
if salario > 1250:
    novo_salario1 = salario * 1.10
    print('Você irá receber um aumento de 10%')
    print(f'O seu novo salário será de R${novo_salario1:.2f}')
else:
    novo_salario2 = salario * 1.15
    print('Você irá receber um aumento de 15%')
    print(f'O seu novo sala´rio será de R${novo_salario2:.2f}')