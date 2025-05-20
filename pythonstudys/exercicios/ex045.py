# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

from random import randint
from time import sleep

bot = 0
player = 0

print('=' * 20)
print('\033[34mJOGANDO JOKENPÔ\033[m')
print('=' * 20)

print('ESSE É UM BOT CRIADO PARA JOGAR JOKENPÔ COM VOCÊ, ESCOLHA UM NÚMERO CORRESPONDENTE A PEDRA, PAPEL OU TESOURA, E JOGUE.')
print('')
print('\033[4;32mCARREGANDO O JOGO.....\033[m')
sleep(2)

print('''\033[33m
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA\033[m
''')
escolha_bot = randint(1,3)
escolha_player = int(input('ESCOLHA O QUE QUER JOGAR: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!!!')
sleep(1)

if escolha_player == 1:
    player = 'PEDRA'
elif escolha_player == 2:
    player = 'PAPEL'
elif escolha_player == 3:
    player = 'TESOURA'
else:
    print('ESTE NÃO É UM VALOR ACEITO NO JOGO!')

if escolha_bot == 1:
    bot = 'PEDRA'
elif escolha_bot == 2:
    bot = 'PAPEL'
elif escolha_bot == 3:
    bot = 'TESOURA'

player = player.lower()
bot = bot.lower()

if bot == player:
    print(f'DEU EMPATE, OS DOIS JOGARAM {player.upper()}')
elif bot == 'pedra' and player == 'papel':
    print(f'VOCÊ GANHOU, O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
    if bot == 'papel' and bot == 'pedra':
        print(f'VOCÊ PERDEU! O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
elif bot == 'pedra' and player == 'tesoura':
    print(f'VOCÊ PERDEU! O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
    if bot == 'tesoura' and player == 'pedra':
        print(f'VOCÊ GANHOU, O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
elif bot == 'tesoura' and player == 'papel':
     print(f'VOCÊ PERDEU! O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
     if bot == 'papel' and player == 'tesoura':
         print(f'VOCÊ GANHOU, O BOT JOGOU {bot.upper()} E VOCÊ {player.upper()}')
