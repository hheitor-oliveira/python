from traceback import print_tb

print('='*10,'DESAFIO 011','='*10)
print('Calcular quantidade de tinta')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = (largura * altura)
print(f'A área da parede é: {area}m²')
print(f'A quantidade de tinta necessária para pintar a parede é de: {area/2}L')