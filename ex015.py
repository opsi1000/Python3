diaria = float(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados?'))
totaldia = diaria * 60.00
totalkm = km*0.15
print('O total a pagar é de R${:.2f}'. format( totalkm + totaldia))
