'''Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50'''
##jeito Thay
print('Os números pares entre 1 e 50 são:')
for c in range(2,51,2):
    print('{}'.format(c))

##jeito Val
print('Os numeros pares entre 1 e 50 são')
for n in range(1,51):
    if n%2 == 0:
        print (n)