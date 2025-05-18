#carro.siga()
#if carro.esquerda():
 #   carro.siga()
 #   carro.direita()
 #   carro.siga()
 #   carro.direita()              # ESTE BLOCO DE COMANDO É CHAMADO DE "BLOCO VERDADEIRO" POIS,
 #   carro.esquerda()             # ELE ACONTECE SE A CONDIÇÃO DO IF FOR VERDADEIRA.
 #   carro.siga()
 #   carro.direita()
 #   carro.siga()
#else:
 #   carro.siga()
 #   carro.esquerda()            # E ESSE BLOCO É CHAMADO DE BLOCO FALSO.
 #   carro.siga()                # E ESSE BLOCO É CHAMADO DE BLOCO FALSO.
 #   carro.esquerda()
 #   carro.siga()
#carro.pare

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

