# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
print('\nProgressão Aritmética (PA)')

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

decimo = primeiro + (10 - 1) * razao

print('Os primeiros 10 termos são:')

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')

print('Fim')
