"""
Desafio 113

Problema: Reencreva a função leiaInt() que fizemos no desafio 104, incluindo agora
          a possibilidade da digitação de um número de tipo inválido.
          Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

Resolução do problema:
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaString(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um nome String válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar.\033[m')
            return 0
        else:
            return n

# Programa principal
n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
