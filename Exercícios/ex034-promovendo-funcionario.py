# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o salário do funcionário: R$'))
aumento = 0

if salario > 1250:
    #novo = salario + (salario * 15 / 100)
    aumento = 0.1
    cor = '\033[34;m'
else:
    aumento = 0.15
    cor = '\033[1;32;m'

print('O aumento foi de {}{:.0f}%\033[m, ou seja, {}R${:.2f}\033[m'.format(
    cor, aumento * 100, cor, salario * aumento))
print('O salário agora é R${:.2f}'.format(salario + salario * aumento))
