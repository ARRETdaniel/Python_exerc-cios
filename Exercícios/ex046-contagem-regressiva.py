# Exercício Python 046: Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
#import emoji
limpa = '\033[m'
azulClaro = '\033[36m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cor = {
    0: '31',
    1: '31',
    2: '31',
    3: '32',
    4: '34',
    5: '33',
    6: '35',
    7: '36',
    8: '37',
    9: '7',
    10: '7;33'
}
for cont in range(10, -1, -1):
    print('\033[{}m{}!\033[m'.format(cor[cont], cont))
    # print('{}'.format(cont))
    # sleep(1)
#print(emoji.emojize('\033[1;33m:collision: FELIZ ANO NOVO!!:collision:'))
print('\033[1;33m FELIZ ANO NOVO!!{}'.format(limpa))
