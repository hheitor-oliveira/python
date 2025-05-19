# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
'''
ATÉ 9 ANOS: MIRIM
ATÉ 14 ANOS: INFANTIL
ATÉ 19 ANOS: JUNIOR
ATÉ 20 ANOS SÊNIOR
ACIMA: MASTER
'''

from datetime import date

print('=' * 20)
print('CATEGORIA DO ATLETA')
print('=' * 20)
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_nascimento
if idade > 20:
    print('SUA CATEGORIA É A MASTER!')
elif idade == 20:
    print('SUA CATEGORIA É SÊNIOR')
elif idade > 15 or idade == 19:
    print('SUA CATEGORIA É JUNIOR')
elif idade == 14 or idade > 9:
    print('SUA CATEGORIA É A INFANTIL')
else:
    print('SUA CATEGORIA É A MIRIM')