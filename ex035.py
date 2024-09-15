# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n1 = int(input('Qual o comprimento da primeira reta? '))
n2 = int(input('Qual o comprimento da segunda reta? '))
n3 = int(input('Qual o comprimento da terceira reta? '))
triangulo  = (n1 + n2 + n3) % 3
if triangulo == 0:
    print('Você digitou {}, {} e {}.\nEsses valores não podem formar um trinagulo, sinto muito!'.format(n1,n2,n3))
else:
    print('Você digitou {}, {} e {}.\nUHUUUUUUUU !!!!!\nCom esses valores digitados conseguimos formar um triangulo!'.format(n1,n2,n3))

'''
print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro segmetno: ')
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR trinângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
'''