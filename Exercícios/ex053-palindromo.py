# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

print('Palíndromos...')  # Título

# Recebe a frase sem espaços antes e depois

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()  # Deixa  frase em caixa alta para evitar erros

frase = frase.replace(' ', '')  # tira os espaços da frase
invertido = ''  # variável que armazenará a frase de tras pra frente

# Laço que roda de trás pra frente para ler os caracters
for c in range(len(frase) - 1, -1, -1):
    # Concatena o caracter em questão à frase invertida
    invertido = '{}{}'.format(invertido, frase[c])

print('\nA frase \033[34m{}\033[m'.format(frase))  # Exibe a frase
print('Ao contrario fica \033[35m{}\033[m, então:'.format(invertido))

if frase == invertido:
    print('\033[33mÉ um palíndromo!')
else:
    print('\033[31mNão é um palíndromo!')

# class code
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1] # fatiamento
'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''
if inverso == junto:
    print('\033[33mÉ um palíndromo!')
else:
    print('\033[31mNão é um palíndromo!')
