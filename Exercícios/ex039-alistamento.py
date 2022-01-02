# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
limpa = '\033[m'
negrito = '\033[1m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'

print('\n{}Checar alistamento!{}\n'.format(negrito, limpa))
print('Informe seu {}Sexo:{}'.format(negrito, limpa))

restart = True
while restart:

    print("""
Digite {1}1{0} para {2}MASCULINO{0}
Digite {1}2{0} para {2}FEMININO{0}
""".format(limpa, amarelo, azul))

    sexo = int(input('{}Opção: {}'.format(negrito, limpa)))

    if sexo == 1:
        nascimento = int(input('Ano de nascimento: '))
        anoAtual = date.today().year
        idade = anoAtual - nascimento
        if idade < 18:
            print('Você só tem {} anos, vai se alistar em {}!'.format(
                idade, nascimento + 18))
            print('Falta(m) {} ano(s)!'.format(18 - idade))
            restart = False
        elif idade == 18:
            print('Você tem {} anos'.format(idade))
            print('Está na hora de se alistar!')
            restart = False
        else:
            print('Você já tem {} anos!'.format(idade))
            print('Deveria ter se alistado em {}'.format(nascimento + 18))
            print('Há {} ano(s) atrás'.format(idade - 18))
            restart = False
    elif sexo == 2:
        print('{}Você não precisa fazer o alistamento obrigatorio!{}'.format(
            amarelo, limpa))
        restart = False
    else:
        print('{}Opção inválida!{}'.format(vermelho, limpa))
        print('\n{}Tente novamente:{}'.format(amarelo, limpa))

# https://www.py4u.net/discuss/20574 - How do I re-run code in Python?

