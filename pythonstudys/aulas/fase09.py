#MANIPULANDO CADEIAS DE TEXTO
#FATIAMENTO DE STRING

frase = 'Curso em vídeo python'
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#ANÁLISE
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#TRANSFORMAÇÃo
print(frase.replace('python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())

frase2 = ('   Aprenda Python  ')

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

#JUNÇÃO
print(' '.join(frase))

frase3 = 'O Henrico É Um Bosta'
lista = ['O', 'Henrico', 'É', 'Um', 'Bosta']
print('-'.join(lista))


