# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta pinta uma área de 2 metros quadrados.

print('. largura e a altura de uma parede\n')
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura*altura
print('\nA parede tem a dimensão de {}m x {}m e  sua área é de {} m².'.format(largura, altura, area))
print('Para pintar esta parede você precisa de {}L de tinta.'.format(area/2))
