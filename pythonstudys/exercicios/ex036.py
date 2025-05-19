'''ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA
   O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS
   ANOS ELE VAI PAGAR.
   CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% OU
   ENTÃO O EMPRÉSTIMO SERÁ NEGADO.'''
from time import sleep

print('\033[4;34mQUER COMPRAR UMA CASA? FAÇA SEU EMPRÉSTIMO AQUI\033[m')
sleep(1)
valor_casa = float(input('Qual é o valor da casa que você quer comprar? '))
sleep(1)
salario_cliente = float(input('Qual é o seu salário atualmente? '))
sleep(1)
prazo_pagamento = int(input('Em quantos anos você pretende pagar o empréstimo? '))
sleep(1)
prestacao = valor_casa / (prazo_pagamento * 12) # FÓRMULA QUE CALCULA A PRESTAÇÃO MENSAL
exceder = salario_cliente * 1.30 - salario_cliente # FÓRMULA QUE CALCULA 30% DO SALÁRIO DO CLIENTE
print('\033[4;33mANALISANDO...\033[m')
sleep(1.5)

if prestacao >= exceder:
    print('Você não poderá fazer esse empréstimo, o valor é muito alto para o seu salário fixo atual!')
else:
    print(f'Analisamos a sua situação, e você PODERÁ fazer esse empréstimo conosco.\nA sua prestação mensal será de \033[1;32mR${prestacao:.2f}\033[m, certo? Muito obrigado por contar conosco')
print('Tenha um ótimo dia!')