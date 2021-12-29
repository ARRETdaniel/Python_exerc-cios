# Exercício Python 028: Escreva um programa que faça o computador "pensar" em
# um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
num = randint(0, 5)
print('\nEu pensei em um numero de 0 a 5, tente advinhar')
chute = int(input('Seu palpite: '))
print('{:-^15}'.format(chute))
print('Processando...')
sleep(1)
print('Acertou! eu pensei em {}'.format(num) if num ==
      chute else 'Errou! eu pensei em {}'.format(num))
print('{:-^15}'.format(chute))
