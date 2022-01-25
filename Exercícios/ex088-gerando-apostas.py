# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

palpites = list()
sorteados = list()

qtJogos = int(input('Quantos jogos dejesa fazer? '))

for count in range(0, qtJogos):
    while len(sorteados) < 6:
        num = randint(1, 60)
        if num not in sorteados:
            sorteados.append(num)
    sorteados.sort()
    palpites.append(sorteados[:])
    sorteados.clear()

print(f'\nSORTEANDO {qtJogos} JOGOS')
for count, jogo in enumerate(palpites):
    print(f'Jogo {count + 1}: {jogo}')
    sleep(0.5)
