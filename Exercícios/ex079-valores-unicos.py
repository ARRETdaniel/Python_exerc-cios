# Exercício Python 079: Crie um programa onde o usuário possa
# digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão
# exibidos todos os valores únicos digitados, em ordem crescente.

# formas de criar listta:
valores = []
valores = list()

while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print(f'Valor {num} adicionado com sucesso...')
    else:
        print('Valor repetido, não vou adicioná-lo...')

    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]

    while opcao not in 'SN':
        opcao = str(input('Por favor, apenas S ou N: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
valores.sort()
print(f'\nVocê digitou os valores {valores}')
