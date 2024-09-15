# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salario atual? '))
aumento = (salario * 0.15)
if salario > 1250.00:
    aumento = (salario * 0.10)
print('PARABÉNS! seu salario teve um aumento de {:.2f} e passará a ser de R${:.2f}.'.format(aumento, (salario + aumento)))

