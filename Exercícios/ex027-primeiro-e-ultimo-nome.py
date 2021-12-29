# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split() # split the data into segments separated by its spaces and add the new data to a list []
index = len(dividido) - 1
print('Primeiro Nome: {}'.format(dividido[0]))
print('Último Nome: {}'.format(dividido[index]))

