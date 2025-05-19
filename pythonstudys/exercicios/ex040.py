# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL
# MÉDIA ABAIXO DE 5.0: REPROVADO
# MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MÉDIA 7.0 OU SUPERIOR: APROVADO

print('=' * 20)
print('MÉDIA ALUNO')
print('=' * 20)

n1_aluno = float(input('Digite a primeira nota do aluno: '))
m2_aluno = float(input('Digite a segunda nota do aluno: '))
media = (n1_aluno + m2_aluno) / 2

if media < 5.0:
    print(f'VOCÊ FOI REPROVADO! SUA MÉDIA FOI {media}, ESTUDE MAIS.')
elif media >= 7.0:
    print(f'PARABÈNS, VOCÊ FOI APROVADO. SUA MÉDIA FOI {media}')
elif media > 5.0 or media == 6.9:
    print(f'VOCÊ ESTÁ DE RECUPERAÇÃO, SUA MÉDIA FOI {media} E FOI INSATISFATÓRIA')