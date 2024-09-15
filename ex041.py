'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
from datetime import date
atual = date.today().year
anoNascimento = int(input('Em qual ano você nasceu? '))
idade = atual - anoNascimento
print (idade)
if idade > 25:
    print('Você nasceu no ano de {} e tem {}, portanto se enquadra na categoria MASTER'.format(anoNascimento, idade))
elif idade < 10:
    print('Você nasceu no ano de {} e tem {}, portanto se enquadra na categoria MIRIM'.format(anoNascimento, idade))
elif idade < 15:
    print('Você nasceu no ano de {} e tem {}, portanto se enquadra na categoria INFANTIL'.format(anoNascimento, idade))
elif idade < 20:
    print('Você nasceu no ano de {} e tem {}, portanto se enquadra na categoria JÚNIOR'.format(anoNascimento, idade))
elif idade < 25:
    print('Você nasceu no ano de {} e tem {}, portanto se enquadra na categoria SÊNIOR'.format(anoNascimento, idade))