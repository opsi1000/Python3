#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual seu nome? ')).strip()
print('O nome digitado tem SILVA em alguma parte? {}'.format('SILVA' in nome.upper()))

