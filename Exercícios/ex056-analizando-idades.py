# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadeTotal = 0
nomeVelho = ''
idadeVelho = 0
menorF = 0
count = 0
for c in range(1, 3):
    print('\n\033[1m----{}ª Pessoa ------\033[m'.format(c))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    count += 1
    idadeTotal += idade

    if sexo == 'M':
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome
    elif sexo == 'F':
        if idade < 20:
            menorF += 1
    else:
        print('\033[31mSexo Inválido\033[m')

media = idadeTotal / count

print('\nMédia de Idade: {:.2f} anos'.format(media))

if nomeVelho != '' and idadeVelho != 0:
    print('O homem mais velho tem {} anos e se chama: {}'.format(
        idadeVelho, nomeVelho))
else:
    print('Nenhum homem!')
if menorF == 0:
    print('Nenhuma mulher com menos de 20 anos!')
elif menorF == 1:
    print('{} mulher com menos de 20 anos!'.format(menorF))
else:
    print('{} mulheres com menos de 20 anos'.format(menorF))
