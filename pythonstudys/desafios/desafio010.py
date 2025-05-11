print('===== DESAFIO 010 =====')
print('Contador de dinheiro')
saldo_reais = int(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com {saldo_reais}R$ você pode comprar {saldo_reais/5.6530:.3f}US$1')

saldo_dolar = int(input('E quantos dólares você tem?'))
print(f'Com {saldo_dolar}US$1 você pode comprar {saldo_dolar*5.65:.3f}R$')
