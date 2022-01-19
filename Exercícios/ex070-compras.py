# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# - A) qual é o total gasto na compra.
# - B) quantos produtos custam mais de R$1000.
# - C) qual é o nome do produto mais barato.
print('\nBalog Store')

count = mil = soma = menor = 0

while True:

    productName = str(input('\nNome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    count += 1
    soma += preco

    if count == 1 or preco < menor:
        barato = productName
        menor = preco

    if preco > 1000:
        mil += 1

    continuar = str(input('Continuar? [S ou N] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(
            input('Por favor, apenas [S ou N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    
print('\nCompra Finalizada!')
print(f'Total gasto: R${soma:.2f}')
print(f'Produtos acima de $1000.00: {mil}')
print(f'O produto mais barato foi: {barato}, que custa: R${menor:.2f}')
