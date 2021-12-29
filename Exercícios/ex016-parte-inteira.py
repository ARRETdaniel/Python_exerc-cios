# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''Neste caso, da pra usar a função nativa int() ao invés de trunc'''

from math import trunc
num = float(input('Digite um número fracionado: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))
print('A parte inteira de {} é {}'.format(num, int(num)))

