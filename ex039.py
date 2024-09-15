'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
idade = int(input('Em que ano vc nasceu? '))
anos = 2024 - idade
if anos < 18:
    print('Calma jovem, vc ainda não tem 18 anos, não está na hora de se alistar, faltam {} anos'.format(18 - anos))
elif anos > 18:
    print('Caraca já passou da hora de você se alistar, deveria ter feito isso à {} anos'.format( anos - 18))
else:
    print('Parabéns, você faz 18 anos essa ano e precisa se alistar!')

    '''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem masceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade ==18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif    idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo =  idade -18
    print('Você já deveria ter se allistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))