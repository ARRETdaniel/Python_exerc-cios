# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

limpa = '\033[m'
azul = '\033[34m'
amarelo = '\033[33m'

print('{:-^40}'.format('Digite dois valores'))

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 == n2:
    print('Os {1}DOIS{0} são {2}IGUAIS!{0}'.format(limpa, amarelo, azul))
elif n1 > n2:
    print('O {1}PRIMEIRO{0} é {2}MAIOR{0} que o {1}SEGUNDO{0}'.format(
        limpa, amarelo, azul))
else:
    print('O {1}SEGUNDO{0} é {2}MAIOR{0} que o {1}PRIMEIRO{0}'.format(
        limpa, amarelo, azul))
