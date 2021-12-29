# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('\nAluguel de Carros\n')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
subDia = dias*60
subKm = km*0.15
print('='*20)
print('{:-^20}'.format('RECIBO'))
#print('       RECIBO  {:-^15}     ')
print('='*20)
print('{} dia(s)   R${:.2f}'.format(dias, subDia))
print('{} km     R${:.2f}'.format(km, subKm))
print('-'*20)
print('TOTAL{:>15.2f}'.format(subDia+subKm))
print('-'*20)
