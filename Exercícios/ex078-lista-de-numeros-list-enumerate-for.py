# Exercício Python 078: Faça um programa que
# leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.
valores = []
for posicao in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {posicao}: ')))

print(f'\nVocê digitou os valores {valores}')

maior = max(valores)
totalMaior = valores.count(maior)
if totalMaior == 1:
    print(f'O maior valor digitado foi {maior}, na posição ', end='')
else:
    print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for posicao, data in enumerate(valores):
    if data == maior:
        print(f'{posicao}... ', end='')

# about: for posicao, data in enumerate(valores):
# https://youtu.be/0LB3FSfjvao?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&t=2056

menor = min(valores)
totalMenor = valores.count(menor)
if totalMenor == 1:
    print(f'\nO menor valor digitado foi {menor}, na posição ', end='')
else:
    print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for posicao, data in enumerate(valores):
    if data == menor:
        print(f'{posicao}... ', end='')
