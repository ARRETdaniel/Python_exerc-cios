# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18, 5: Abaixo do Peso
# - Entre 18, 5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
cor = {
    'limpa': '\033[m',
    'imc': '\033[1;33m',
    'value': '\033[1;34m',
    'text': '\033[1;30m'
}
print('Calculadora de {}IMC{}'.format(cor['imc'], cor['limpa']))

peso = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)

print('Seu {1}IMC{0} é {2}{3:.1f}{0}'.format(
    cor['limpa'], cor['imc'], cor['value'], imc))

if imc > 1 and imc <= 18.5:
    classificacao = 'Abaixo do Peso'
elif imc > 18.5 and (18.5 <= imc < 25):
    classificacao = 'Peso ideal'
elif imc > 25 and (25 <= imc < 30):
    classificacao = 'Sobrepeso'
elif imc > 30 and (30 <= imc < 40):
    classificacao = 'Obesidade'
elif imc >= 40:
    classificacao = 'Obesidade Mórbida'
else:
    classificacao = 'UNDEFINED'

print('Classificação: {}{}{}'.format(cor['text'], classificacao, cor['limpa']))
