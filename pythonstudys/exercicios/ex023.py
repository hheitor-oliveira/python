# Faça um programa que leia um número de 0 a 9999  e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

n1 = input('Digite um número de 0 a 9999: ')
n2 = n1.isnumeric()
formatacao = n1.zfill(4)
formatacao = formatacao.replace('', ' ')
lista_numero = formatacao.split()

if n2 == True and len(lista_numero) <= 4:
    print(
        f'Milhar: {lista_numero[-4]}\nCentena: {lista_numero[-3]}\nDezena: {lista_numero[-2]}\nUnidade: {lista_numero[-1]}'
    )
else:
    print('Este erro é exibido quando o número passa de 9999 ou não é um número. Tente Novamente.')

