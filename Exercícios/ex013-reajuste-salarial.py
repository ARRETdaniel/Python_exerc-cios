# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('\nReajuste Salarial\n')
salario = float(input('Qual é o salario do funcionário? R$'))
aumentado = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(
    salario, aumentado))
