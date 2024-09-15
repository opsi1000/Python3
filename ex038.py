'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

numero1 = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite o segundo numero? '))
if numero1 > numero2:
    print('O primeiro valor é maior que o segundo valor')
elif numero2 > numero1:
    print('O segundo valor é maior que o primeiro valor')
else:
    print('Ambos os valores são iguais!!')