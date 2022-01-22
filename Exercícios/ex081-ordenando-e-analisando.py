# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, somente S ou N: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
if len(lista) != 1:
    print(f'Você digitou {len(lista)} valores')
    copia = lista[:]
    copia.sort(reverse=True)
    print(f'Os valores digitados, em ordem decrescente, foram: {copia}')
else:
    print(f'Você digitou 1 valor: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado ', end='')
    if lista.count(5) == 1:
        print(f'uma vez, na posição {lista.index(5)}')
    else:
        print(f'{lista.count(5)} vezes, nas posições ', end='')
        for c, v in enumerate(lista):
            if v == 5:
                print(f'{c}... ', end='')
else:
    print('O valor 5 não foi digitado')
