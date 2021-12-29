# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade: ')).strip()
print('A cidade termina com santo? {}'.format(
    'santo' in cidade.lower().split()[1]))
