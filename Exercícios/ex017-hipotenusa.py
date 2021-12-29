# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
print('\nPyth-Ágoras\n')
cat1 = float(input('Medida de um cateto: '))
cat2 = float(input('Medida do outro cateto: '))
# Sem a biblioteca math:
print('\nA hipotenusa mede {}'.format(((cat1 ** 2) + (cat2 ** 2)) ** (1/2)))
# Com a biblioteca math:

print('\nA hipotenusa mede {:.2f}'.format(hypot(cat1, cat2)))
