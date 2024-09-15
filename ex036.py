'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Informa o valor do imovel: '))
salario = float(input('Qual a sua renda mensal? '))
tempo = int(input('Em quantos anos vc pretende financiar? '))
parcela = casa /  ( tempo * 12)
custo = salario * 30 / 100
print(parcela)
print(custo)

print('Para conseguir financiar uma casa no valor de R${:.2f}, sua renda mensal deve ser de R${:.2f}, para poder arcar com a parcela no valor de R${:.2f}'.format(casa,custo + (custo *70/100) , custo))
if parcela > custo:
    print('Não é possivel realizar a compra, pois o salario não é compativel')
else:
    print('Parabéns, você vai conseguir comprar sua casa. Sua parcela é de R${:.2f}'.format(custo))


'''
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anosde financiamento? '))
prestação = casa (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
'''