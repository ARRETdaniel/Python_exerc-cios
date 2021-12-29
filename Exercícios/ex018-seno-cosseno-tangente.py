# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
print('\nSeno, Cosseno e Tangente\n')
angulo = float(input('Digite um ângulo em graus: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('\nÂngulo: {}'.format(angulo))
print('Seno:{:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
