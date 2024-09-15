'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''
altura = float(input('Qual a sua altura: '))
peso = float(input('Qual o seu peso: '))
imc = peso / (altura**2)

print('Seu peso é {:.0f} e sua altura é {:.2f}m, seu IMC é de {:.2f} que se enquadra no status '  .format(peso, altura, imc ),end='')
if imc > 39:
    print('Obesidade Mórbida')
elif imc > 29:
    print('Obesidade')
elif imc > 24:
    print('Sobrepeso')
elif imc > 18.4:
    print('Peso Ideal')
else:
    print('Abaixo do Peso')