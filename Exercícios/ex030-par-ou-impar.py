# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('\nÉ par ou impar?')
x = int(input('Digite um número: '))
if x % 2 == 0:
    print('{} é um número PAR'.format(x))
else:
    print('{} é um número ÍMPAR'.format(x))
