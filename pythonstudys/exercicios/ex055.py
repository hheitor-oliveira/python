# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS
lista = []

for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    lista.append(peso)
print(f'De todos os pesos das pessoas digitadas, a mais pesada tem {max(lista):.2f}KG')