# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
linha = []

for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um número para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

print(type(matriz))
print(matriz)

for c in matriz:
    for i in c:
        print(f'[ {i:^3} ]', end='')
    print()

# profe solution
'''
matriz = [[],[],[]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]' , end='')
    print()

'''
