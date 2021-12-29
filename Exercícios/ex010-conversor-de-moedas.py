print('\nConversor de Moedas\n')
real = float(input('Quantos reais você tem? R$'))
dolares = real/5.67
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolares))
