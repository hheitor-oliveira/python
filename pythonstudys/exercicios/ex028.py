# ESCREVA UM PROGRAMA QUE FAÇA O COMPTUADOR 'PENSAR' EM UM NÚMERO INTEIR ENTRE 0 E 5 E
# PEÇA PARA O USÚARIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENDEU OU PERDEU

from random import randint
from time import sleep
print('Este é um jogo de adivinhação com a máquina. Se divirta!')
sleep(1)
print('O jogo é simples, o computador irá escolher um número de 0 a 5, e você terá que adivinhar, se acertar o número, você ganha.')
sleep(1)
n1_maquina = randint(0, 5) # FAZ O COMPUTADOR PENSAR EM UM NÚMERO
print('O computador já escolheu um número, e você? Digite-o abaixo.')
n1_player = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
verificacao = n1_player.is_integer()

if n1_player == n1_maquina and verificacao == True:
    print('PARABÉNS! Você me venceu!')

elif n1_player == False:
    print('Isso não é um número, escreva um número e tente novamente.')

elif n1_player > 5:
    print('O número é maior que 5.\nJogue direito!')

else:
    print(f'EU GANHEI! Eu pensei no {n1_maquina} e não no {n1_player}!')