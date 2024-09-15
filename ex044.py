'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:


– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

'''
produto = float(input('Qual o valor do produto? '))
forma_pagamento = int(input('Escolha a forma de pagamento: \n[1] - Dinheiro/Cheque\n[2] - Cartão\n'))
if forma_pagamento == 2:
    parcelas = int(input('Escolha em quantas vezes quer parcelar:\n[1] - A vista (1x)\n[2] - Parcelado em 2 vezes\n[3] - Parcelado em 3 ou mais vezes\n'))
    if parcelas == 1:
        pagamento = produto - ( (produto * 5) / 100 )

    elif parcelas ==2:
        pagamento = produto
    elif parcelas ==3:
        pagamento = produto + ((produto * 20) / 100)
    else:
        print('O valor digitado não é um valor valido')
else:
    pagamento = produto - ((produto * 10) / 100)

print('O produto que você comprou custa R${:.2f} e o valor final é de R${:.2f}'.format(produto, pagamento))