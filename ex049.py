'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
numero = int(input('Digite um numero para montarmos a tabuada: '))
for n in range(1,11):
    print('{} X {} = {}'.format(numero, n, (numero * n)))