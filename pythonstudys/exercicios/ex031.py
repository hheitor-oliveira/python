# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM COBRANDO
# R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.

distancia_viagem = float(input('Qual é a distância da viagem que você irá fazer? '))
verificacao = distancia_viagem.is_integer()
print(f'A distância da viagem é de {distancia_viagem}KM')
if verificacao == True and distancia_viagem <= 200:
    preco_viagem = distancia_viagem * 0.50
else:
    preco_viagem = distancia_viagem * 0.45

if distancia_viagem <= 200:
    print(f'O valor cobrado pela sua viagem é de R${preco_viagem}')
else:
    print(f'Sua viagem é longa, logo foi feito um desconto! O valor ficará de R${preco_viagem}')