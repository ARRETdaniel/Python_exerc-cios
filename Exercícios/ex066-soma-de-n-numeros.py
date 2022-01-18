# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
limpa = '\033[m'
verm = '\033[31m'
amar = '\033[33m'
azul = '\033[34m'

print(
    f'\nA qualquer momento digite {amar}999{limpa} para {verm}cancelar{limpa} o programa\n')

count = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    count += 1

if count > 1:
    plural = 's'
else:
    plural = ''

print(f'\n{azul}{count}{limpa} número{plural} digitado{plural}')
print(f'A soma vale {azul}{soma}{limpa}')
