# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = int(input('Digite um número: '))

count = 1
maior = menor = soma = num
continuar = 'S'

while continuar == 'S':
    
    continuar = str(input('Deseja inserir mais números? [S/N] ')).strip().upper()[0]

    if continuar == 'S':
        num = int(input('Digite mais um número: '))

        if num > maior:
            maior = num

        if num < menor:
            menor = num
        soma += num
        count += 1

print('{} números digitados'.format(count))
print('A média entre eles foi {:.2f}'.format(soma / count))
print('O maior número foi {}'.format(maior))
print('O menor foi {}'.format(menor))
