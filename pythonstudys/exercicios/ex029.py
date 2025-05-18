''' ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
 SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
 A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.'''

vel = float(input('Qual a velocidade do seu carro? '))
print(f'A velocidade do seu carro é de {vel}KM/h')

if vel > 80:
    print('Você está acima do limite da rodovia! Você irá ser multado.')
    multa = (vel - 80) * 7
    print(f'A multa aplicada ao seu veículo, foi de R${multa}.')
else:
    print('Você está abaixo do limite de velocidade. Continue assim, e atenção ao trânsito')
