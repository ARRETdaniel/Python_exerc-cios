# Exercício Python 060: Faça um programa que leia um número qualquer
# e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial


num = int(input('Digite um número inteiro para exibir eu fatorial: '))

f = factorial(num)  # using method from math.factorial
print('{} fatorial é {} (using method)'.format(num, f))

''' using for 
for c in range(1, num + 1):
    fatorial *= c
'''
c = num
fatorial = 1
while c > 0:

    #fatorial *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(fatorial), end='')
    fatorial *= c
    c -= 1

print('\n{} fatorial é {}'.format(num, fatorial))
