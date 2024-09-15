'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''

numero = int(input('Digite um numero: '))
tipo = numero%2
if tipo == 0:
    print('O numero digitado foi {}, e ele é um numero PAR'.format(numero))
else:
    print('O numero digitado foi {}, e ele é um numero IMPAR'.format(numero))