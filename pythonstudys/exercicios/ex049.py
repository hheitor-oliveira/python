# REFAÇA O DESAFIO 009 MOSTRANDO A TABUADA DE UM NÚMERO QUE O USÚARIO ESCOLHE, SÓ QUE AGORA UTILIZANDO O LAÇO FOR.
tabuada = int(input('Digite qualquer número para obter sua tabuada: '))
for c in range(1, 11):
    print(f'{tabuada} X {c} = {tabuada * c}')