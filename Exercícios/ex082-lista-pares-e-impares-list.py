# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    while opcao not in 'SN':
        opcao = str(input('Por favor, somente [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue

for num in lista:
    if (num % 2) == 0:
        pares.append(num)
    else:
        impares.append(num)
'''
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
'''
print(f'A lista \033[34mCOMPLETA\033[m é {lista}')
print(f'A lista de números \033[34mPARES\033[m é {pares}')
print(f'A lista de números \033[34mÍMPARES\033[m é {impares}')
