# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('\nConversor de Temperaturas\n')
c = float(input('Temperatura em ºC: '))
f = (c * 9 / 5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(c, f))
