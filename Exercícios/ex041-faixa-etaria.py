# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

cor = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'title': '\033[1;30m',
    'danger': '\033[7;31m'
}

print('\nConfederação Nacional de Natação')

nascimento = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - nascimento

if idade > 1 and idade <= 9:
    categoria = [cor['azul'], 'Mirim']
elif idade > 9 and idade <= 14:
    categoria = [cor['azul'], 'Infantil']
elif idade > 14 and idade <= 19:
    categoria = [cor['azul'], 'Junior']
elif idade > 19 and idade <= 25:
    categoria = [cor['azul'], 'Sênior']
elif idade > 25 and idade <= 130:
    categoria = [cor['azul'], 'Master']
else:
    categoria = [cor['danger'], 'Invalido']

print('O atleta tem {}{} anos{}'.format('\033[33m', idade, '\033[m'))
print('Sua categoria é: {}{}'.format(categoria[0], categoria[1].upper()))
