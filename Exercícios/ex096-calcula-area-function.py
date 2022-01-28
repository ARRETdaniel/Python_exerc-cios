"""
Desafio 096

Problema: Faça um programa que tenha uma função chamada area(), que receba as dimeções
          de um terreno retangular(largura e comprimento) e mostre a área do terreno.

Resolução do problema:
"""


# Função para impressão de cabeçalho
def header(mensagem):
    print('-' * 30)
    print(f'{mensagem:^30}')
    print('-' * 30)


# Função para calcular area do terreno
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {area}m²')

# resposta do Gustavo


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2.')

# Programa principal


large = float(input('LARGURA (m): '))
compri = float(input('COMPRIMENTO (m) '))

header('Área de Terreno')
area(large, compri)
