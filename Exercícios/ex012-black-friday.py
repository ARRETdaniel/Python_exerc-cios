# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('\nBlack Friday!\n')
preco = float(input('Qual é o preço do produto? R$'))
descontado = preco - (preco * 0.05)
print('\nVocê ganhou 5% de desconto! \no produto que custava R${:.2f} vai custar R${:.2f}'.format(
    preco, descontado))

