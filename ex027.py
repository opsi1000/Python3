#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
n = str(input('Qual o seu nome? ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu útilmo nome é {}'.format(nome[len(nome)-1]))

