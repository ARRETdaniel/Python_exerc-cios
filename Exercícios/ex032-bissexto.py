# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('\nÉ bissexto?')
ano = int(input('Digite um ano ou coloce 0 (zero) para pegar o ano atual: '))
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
if ano == 0:
    ano = date.today().year
b6 = False
if ano % 400 == 0:
    b6 = True
else:
    if ano % 100 == 0:
        b6 = False
    elif ano % 4 == 0:
        b6 = True
print('\nO ano {}'.format(ano))
print('É' if b6 else 'Não é', end=' bissexto\n')
