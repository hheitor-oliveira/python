# ESCREVA UM PROGRAMA QUE LEIA UM NÚERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESOCLHER QUAL SERÁ A BASE DE CONVERSÃO
from time import sleep

print('=' * 20)
print('CONVERSOR NUMÉRICO')
print('=' * 20)
sleep(1)
num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
\033[34m[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL\033[m''')
opcao = int(input('Escolha a sua opção: '))
sleep(1)
print('\033[4;33mFAZENDO A CONVERSÃO\033[m')
sleep(2)
if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convetido para OCTAL é {oct(num[2:])}')
elif opcao == 3:
    print(f'O número {num} convetido para HEXADECIMAL é {hex(num[2:])}')
elif opcao > 3 or opcao == 0:
    print('Este valor não é aceito! Insira um valor válido')