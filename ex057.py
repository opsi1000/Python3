#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
conclusao = 0

while conclusao != 1:
    genero = str(input('Digite o seu genero [F/M]: ')).upper()
    if genero != 'F' and genero != 'M':
        input('Valor digitado inválido, por favor digite novamente.')
    else:
        conclusao = 1
print('O valor digitado foi {}'.format(genero))
