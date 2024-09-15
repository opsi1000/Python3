'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2


if media >7:
    print('Parabéns sua média é de {:.1f} e vc foi APROVADO'.format(media))
elif media >= 5:
    print('Cuidado, sua média é de {:.1f} e vc está em RECUPERAÇÃO'.format(media))
else:
    print('Sa média é de {:.1f}, com isso você foi REPROVADO'.format(media))