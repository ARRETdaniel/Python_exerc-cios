"""
Desafio 100

Problema: Faça um programa que tenham uma lista chamada numeros e duas funções
          chamadas sorteia() e somaPar().
          A primeira função vai sortear 5 números e vai coloca-los dentro da lista
          e a segunda função vai mostrar a soma entre todos valores pares sorteados
          pela função anterior.

Resolução do problema:
"""
from time import sleep
from random import randint


def sorteia():
    print('Sorteando 5 valores para lista --> ', end='')
    for cont in range(5):
        valorSorteado = randint(1, 10)
        numeros.append(valorSorteado)
        print(f'{valorSorteado}', end=' ')
    print('Prontinho...')


def soma_par(lista_valores):
    par = 0
    for valor in lista_valores:
        if valor % 2 == 0:
            par += valor

    print(
        f'A soma de todos valores pares de: {lista_valores}, é igual a --> {par}')


def sorteia(lista):  # 2a. criar a funcao sorteia() , 5a. a funcao sorteia recebe lista como parametro
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):  # 6o. cria for para escolher os numeros
        n = randint(1, 10)  # 7o. variavel n recebe randint de 1 ate 10
        # 8o. colocar na lista os numeros sorteados da variavel n
        lista.append(n)
        print(f'{n} ', end='')  # 9o. imprimir os valores sorteados
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):  # 3a. criar a funcao somaPar() recebendo a lista e coloca-la como comentario
    soma = 0  # 11o. criar uma variavel com 0
    for valor in lista:  # 12o. for para verificar se o numero é PAR
        if valor % 2 == 0:
            soma += valor
    # 13o. Mostrar a lista e a soma dos PARES
    print(f'Somando os valore PARES de {lista}, temos {soma}')


# Programa Principal

numeros = []
sorteia()
soma_par(numeros)
numeros = list()  # 1a. criar uma lista vazia de numeros
sorteia(numeros)  # 4a. chamar a funcao sorteia
somaPar(numeros)  # 10o. chamar a funcao somaPar
