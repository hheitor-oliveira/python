# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO. CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
from time import sleep

print('\033[34m=' * 20)
print('CONDIÇÕES DE PAGAMENTO')
print('=' * 20)

# PEGANDO O VALOR INICIAL DO PRODUTO
produto = float(input('\033[mColoque ao lado, o preço do produto: '))
print('\033[32mCARREGANDO...\033[m')
sleep(2)


# PAINEL DE ESCOLHA DE FORMA DE PAGAMENTO
print('''\033[4;33m
[ 1 ] À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
[ 2 ] À VISTA NO CARTÃO: 5% DE DESCONTO
[ 3 ] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
[ 4 ] 3X OU MAIS NO CARTÃO: 20% DE JUROS\033[m
''')
opc = int(input('Escolha a forma de pagamento, digite o número correspondente: '))
print('\033[32mCARREGANDO...\033[m')
sleep(2)

# CONDIÇÕES CONFORME A ESCOLHA ACIMA
if opc == 1:
    produto = produto * 0.90
    print(f'Comprando o produto à vista no dinheiro ou no cheque, você recebe 10% DE DESCONTO! E o valor do produto ficara R${produto:.2f}')
elif opc == 2:
    produto = produto * 0.95
    print(f'Comprando o produto à vista no cartão, você recebe 5% DE DESCONTO, e o valor do produto ficara R${produto:.2f}')
elif opc == 3:
    produto = produto / 2
    print(f'Comprando o produto em até 2X NO CARTÃO, você pagara R${produto:.2f} em DOIS MESES!')
elif opc == 4:
    parcelas = int(input('Em quantas vezes você irá parcelar o produto? '))
    if parcelas <= 2:
        print('Você \033[31mNÃO PODE\033[m parcelar em menos de 3X com esta forma de pagamento!')
    elif parcelas >= 3:
        produto = produto * 1.20
        produto = produto / parcelas
        print(f'Comprando o produto em {parcelas} PARCELAS, você irá pagar R${produto:.2f} por {parcelas} meses!')