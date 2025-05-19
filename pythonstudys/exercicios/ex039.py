# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
# SE É A HORA DE SE ALISTAR
# SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
print('=' * 20)
print('ALISTAMENTO EXÉRCITO')
print('=' * 20)
ano_nascimento = int(input('Em que ano você nasceu? '))
idade_pessoa = 2025 - ano_nascimento
if idade_pessoa < 18:
    print(f'A idade para se alistar no exército é 18 anos, portanto você ainda não pode se alistar.')
    print(f'Ainda faltam {18 - idade_pessoa } para você poder se alistar!')
elif idade_pessoa == 18:
    print(f'VOCÊ PRECISA SE ALISTAR ESSE ANO! Você já completou {idade_pessoa} anos!!')
elif idade_pessoa == 19:
    print(f'JÁ PASSOU DA HORA! FAZ {idade_pessoa - 18} ANO QUE VOCÊ DEVERIA TER SE ALISTADO')
else:
    print(f'JÁ PASSOU DA HORA! FAZEM {idade_pessoa - 18} ANOS QUE VOCÊ DEVERIA TER SE ALISTADO')