# Exercício Python 074: Crie um programa que vai gerar cinco números
# aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
#
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = numeros[0]

print(f'Os números sorteados foram:', end=' ')

for num in numeros:
    print(num, end=' ')
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# Da pra usar o sorted(), desta forma:
menor = sorted(numeros)[0]
maior = sorted(numeros)[-1]

# Ou ainda, de forma mais simples:
menor = min(numeros)
maior = max(numeros)

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
