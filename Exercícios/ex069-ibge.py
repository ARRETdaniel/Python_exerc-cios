# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
print('\nIBGE - Instituto Balog Gardino de Estatística')

maiores = totfame = homens = 0

while True:
    print('\nCadastre uma Pessoa')

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M ou F] ')).strip().upper()[0]

    while sexo not in 'FM':
        sexo = str(input('Por favor, apenas [M ou F]: ')).strip().upper()[0]

    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        totfame += 1

    continuar = str(input('\nQuer continuar? [S ou N] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(
            input('Por favor, apenas  [S ou N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\nPesquisa Encerrada!')
print(f'Pessoas maiores de 18 anos: {maiores}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {totfame}')
