# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Digite 3 números:')
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
'''
maior = ''
menor = ''
if a > b:
    maior = a
    menor = b
    if a > c:
        maior = a
        if b > c:
            menor = c
        else:
            menor = b
    else:
        maior = c
else:
    maior = b
    menor = a
    if b > c:
        maior = b
        if c > a:
            menor = a
        else:
            menor = c
    else:
        maior = c
'''
# verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número é {} e o menor é {}'.format(maior, menor))
