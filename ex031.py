'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
viagem = float(input('Qual a distância que sua viagem possui? '))
if viagem <= 200:
    print('FAÇA UMA BOA VIAGEM! Sua passagem tera o valor de R${:.2f}! Esse é o preço para a distância percorrida de {}Km'.format(viagem * 0.50, viagem))
else:
    print('FAÇA UMA BOA VIAGEM! Sua passagem tera o valor de R${:.2f}! Esse é o preço para a distância percorrida de {}Km'.format(viagem * 0.45, viagem))



#distancia = float(input(''))