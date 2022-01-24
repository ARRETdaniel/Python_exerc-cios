# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

principal = list()
temporario = list()
maior = menor = 0

while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))

    principal.append(temporario[:])
    if len(principal) == 1:
        maior = temporario[1]
        menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]

    temporario.clear()
    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, somente [S ou N]')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
print(f'Ao todo, você cadastrou {len(principal)} ', end='')
print('pessoas' if len(principal) > 1 else 'pessoa')

print(f'O maior peso foi {maior} Kg, peso de ', end='')
for peso in principal:
    if peso[1] == maior:
        print(peso[0], end='; ')

print(f'\nO menor peso foi {menor} Kg, peso de ', end='')
for peso in principal:
    # o peso la lista esta em: ["nome", peso] logo: peso[1]
    if peso[1] == menor:
        print(peso[0], end='; ')
