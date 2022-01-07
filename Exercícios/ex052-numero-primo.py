# Exercício Python 052: Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.
print('\nÉ primo?')

num = int(input('Digite um número: '))

saldo = 0

for c in range(num, 0, -1):
    if num % c == 0:
        saldo += 1

if saldo == 2:
    print('\033[33mÉ primo!')
else:
    print('\033[31mNão é primo!')


tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'. format(c), end=' ')
print('\n \033[m O num {} foi divisivel {} vezes'. format(num, tot))

if tot == 2:
    print('\033[33mÉ primo!')
else:
    print('\033[31mNão é primo!')
