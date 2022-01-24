# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = []
linha = []
somaPar = somaTer = maior = somaTerc = 0

for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um número para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

for indexLinha, linha in enumerate(matriz):
    for coluna, termo in enumerate(linha):
        print(f'[ {termo:^3} ]', end='')
        if termo % 2 == 0:
            somaPar += termo
        if coluna == 2:
            somaTer += termo
        if indexLinha == 1:
            if coluna == 0 or termo > maior:
                maior = termo
    print()

# sina dis vakires terceira coluna
for l in range(0, 3):
    somaTerc += matriz[l][2]

print(f'Soma dos números pares: {somaPar}')
print(f'Soma da terceira coluna: {somaTer}')
print(f'Soma da terceira coluna: {somaTerc}')
print(f'{maior} é o maior valor da segunda linha')
