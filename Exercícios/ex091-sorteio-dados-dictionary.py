# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

from sympy import together

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6), }

ranking = list()

print('Drawn values: ')
for k, v in jogo.items():
    print(f'{k} Drawn the die: {v}')
    sleep(0.1)
    # itemgetter coloca o dict na order selecionada. Neste caso em ordem de valor. (1)
    # reverse colocar o valor ordenado em ordem do maior para menor.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-+' * 20)
print('Players Rank')
for i, v in enumerate(ranking):
    print(f'  {i+1}a place: {v[0]} with: {v[1]}.')
    sleep(0.1)
