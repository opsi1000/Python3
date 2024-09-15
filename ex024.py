# Crie um programa que leia o nome de uma cidade diga se ela começa ou nao com o nome "SANTO"
cidade = str(input('Digite o nome de uma cidade: '))
comeca = cidade.split()
val = 'SANTO' in comeca
print (val)
#Modo guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')