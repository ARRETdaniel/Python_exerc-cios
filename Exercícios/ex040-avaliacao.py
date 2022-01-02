# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
limpa = '\033[m'
negrito = '\033[1m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'

print('\nDigite as duas notas do aluno:')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media < 5:
    status = "\033[31mREPROVADO\033[m"
elif 5 <= media < 7:
    status = "\033[33mEM RECUPERAÇÃO\033[m"
elif media >= 7:
    status = "\033[34mAPROVADO\033[m"
print('A média do aluno foi {:.1f}, portanto está {}!'.format(media, status))
