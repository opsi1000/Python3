'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
carro = float(input('Qual a velocidade que o carro está? '))
excedente = carro - 80.00
multa = 7.00
if carro > 80.00:
    print('O carro está em uma velocidade de {:.2f}Km, e será multado no valor de R${:.2f}'.format(carro, multa*excedente))


'''   Resolução do problema pelo guanabara
velocidade =    float(input('Qual é a velocidade que o carro está? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!')
'''