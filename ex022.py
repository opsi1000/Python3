"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
 O nome com todos minusculas
 quantas letras ao todo (sem considerar espaços)
quantas letras tem o primeiro nome """

nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('O nome tem {} caracteres' .format(  len( nome.replace(' ',''))))
primeiroNome = nome.split()
print('O primeiro nome é {} e tem {} caracteres'.format( primeiroNome[0], len(primeiroNome[0])))