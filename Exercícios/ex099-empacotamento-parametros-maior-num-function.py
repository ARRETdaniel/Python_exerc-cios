"""
Desafio 099

Problema: Faça um programa que tenha a função maior(), que recebe vários parâmetros
          com valores inteiros.
          Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

Resolução do problema:
"""
from time import sleep


# Função para impressão de barra
def barra():
    print('-' * 50)


# resposta do Gustavo


def maior(*args):  # * informa que irei receber varios parametros e irei
    # "desempacota-los" utilizando estrutura de repericao
    barra()
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in args:
        print(f'{valor} ', end='', flush=True)
        sleep(0.1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    #print(f'Maior valor: {max(num)}')


# https://youtu.be/1TbOk_r3eYc
# Empacotamento e desempacotamento de parâmetros
lista = [2, 9, 4, 5, 7, 1, 2, 9, 4, 5, 7, 1]
maior(lista)
maior(*lista)
# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
