#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
achou = frase.count('A')
print ( 'A frase possui {} letras A'.format( achou))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {} '.format(frase.rfind('A')+1))
