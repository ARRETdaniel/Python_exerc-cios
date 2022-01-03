# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

cor = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'title': '\033[1;30m',
    'danger': '\033[7;31m'
}

print('\nDigite a medida de 3 segmentos para saber se podem formar um triângulo')
r1 = float(input('Primeiro segmento: '))
f2 = float(input('Segundo segmento: '))
f3 = float(input('Terceiro segmento: '))

if f2 - f3 < r1 < r1 + f2 and r1 - f3 < f2 < r1 + f3 and r1 - f2 < f3 < r1 + f2:
    # r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == f2 == f3:
        tipo = 'EQUILÁTERO'
    elif r1 == f2 or r1 == f3 or f2 == f3:
        tipo = 'ISÓSCELES'
    else:  # r1 != r2 != r3 != r1:
        tipo = 'ESCALENO'
    print('Estes segmentos podem formar um triangulo: {}{}{}'.format(
        cor['azul'], tipo.upper(), cor['limpa']))

else:
    print('{}Estes segmentos não podem formar um triângulo{}'.format(
        cor['danger'], cor['limpa']))
