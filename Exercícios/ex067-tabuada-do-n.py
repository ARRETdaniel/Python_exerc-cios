# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
limpa = '\033[m'
verm = '\033[31m'
amar = '\033[33m'
azul = '\033[34m'

print(
    f'A qualquer momento digite um um número {amar}negativo{limpa} para {verm}encerrar o programa{limpa}')

while True:
    num = int(input('Quer ver a tabuada de que valor? '))

    if num < 0:
        break
    print(f'{num:-^15}')
    c = 1

    '''
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    '''

    while c <= 10:
        print(f'{num} x {c} = {num * c}')
        c += 1
    print('-' * 15)

print(f'{azul}Programa Tabuada v3.0 encerrado{limpa}')
