"""Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex digite um numero: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
separador = int(input('Digite um numero entre 0 a 9999: '))
u = separador // 1 % 10
