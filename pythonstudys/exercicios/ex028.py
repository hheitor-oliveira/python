# ESCREVA UM PROGRAMA QUE FAÇA O COMPTUADOR 'PENSAR' EM UM NÚMERO INTEIR ENTRE 0 E 5 E
# PEÇA PARA O USÚARIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENDEU OU PERDEU

from random import randint

print('Este é um jogo de adivinhação com a máquina. Se divirta!')
print('O jogo é simples, o computador irá escolher um número de 0 a 5, e você terá que adivinhar, se acertar o número, você ganha.')
n1_maquina = randint(0, 5)
print('O computador já escolheu um número, e você? Digite-o abaixo.')
n1_player = int(input('Digite um número de 0 a 5: '))
verificacao = n1_player.is_integer()

if n1_player == n1_maquina and verificacao == True:
    print('Você acertou o número, você ganhou!')

elif n1_player == False:
    print('Isso não é um número, escreva um número e tente novamente.')

elif n1_player > 5:
    print('O número é maior que 5.\nJogue direito!')

else:
    print('Você errou o número, você perdeu!')