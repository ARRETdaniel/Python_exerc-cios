# Exercício Python 035: Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Digite o comprimento de 3 retas:')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
existe = False
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    existe = True
print('É' if existe else 'Não é', end=' um triângulo')

