#nome = str(input('Qual é o seu nome? '))
#if nome == 'Gustavo':
    #print('Que nome lindo você tem!')
#else:
    #print('Seu nome é tão normal!')
#print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota: ' ))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2) / 2
print(f'A sua média foi {n}')

if n >= 8:
    print('Sua nota foi ótima!')
elif n >= 6:
    print('Sua nota foi boa!')
else:
    print('Sua nota foi ruim, estude mais!')