# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS E NO FINAL MOSTRE QUANTAS PESSOAS
# AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
ano = 2025
maior = 0
menor = 0

for c in range(1,7):
    nasc = int(input(f'Digite o {c}° ano de nascimento: '))
    if ano - nasc >= 18:
        maior += 1
    elif ano - nasc <= 17:
        menor += 1
print(f'Dos 7 valores digitados, {maior} pessoas já atingiram a maioridade')
print(f'E {menor} ainda não atingiram a maioridade')