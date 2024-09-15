#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
lista = [n1,n2,n3]
lista.sort()
print ('Você digitou os numeros: {},{} e {}, dentre eles o menor é o {} e o maior é o {}'. format(n1,n2,n3, min(lista), max(lista)))

'''   Essa é a versão do guanabara
a = int(input('Primeiro numero'))
b = int(input('Segundo numero:'))
c = int(input('Terceiro numero'))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c< b:
    menor = c
# Verificando quem é o maior
maior = a
if b> a and b>c:
    maior = a
if c> a and c> b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

'''