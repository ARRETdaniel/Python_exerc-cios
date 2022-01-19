# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('\nARRET Bank')

notas = {
    1: 50,
    2: 20,
    3: 10,
    4: 1
}

saque = int(input('Qual o valor a ser sacado? R$'))

for c in range(1, 5):

    n = saque // notas[c]

    if n > 0:
        print(f'{n} notas de R${notas[c]:.2f}')
        saque = saque % notas[c]
    if saque == 0:
        break
