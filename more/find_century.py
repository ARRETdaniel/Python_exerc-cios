# O primeiro século vai do ano 1 até e incluindo o ano 100,
# o segundo século - do ano 101 até e incluindo * o ano 200, etc.
# Dado um ano, retorne o século em que ele se encontra.

limpa = '\033[m'
negrito = '\033[1m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'


def retorne_seculo(ano):

    # valores negativos nao sao levados em conta
    if (ano <= 0):
        print(f'Ano {vermelho}{ano}{limpa} nao valido')
    # O primeiro século vai do ano 1 até e incluindo o ano 100
    elif (ano <= 100):
        print(f'Seculo: {negrito}1{limpa}')
    # resto da divisao igual a 0
    elif ((ano % 100) == 0):
        print(f'Seculo:{amarelo}', (ano // 100), f'{limpa}')
    # se a divisao tiver resto Ex: ano 1705 % 100 = 5,
    #  (1705 // 100) + 1 = 18
    else:
        print(f'Seculo:{azul}', ((ano // 100) + 1), f'{limpa}')


# ano
ano = [-1, 1, 101, 1705, 1900, 200, 1601, 2000, 2001, -5]
for i in range(0, len(ano)):
    retorne_seculo(ano[i])
