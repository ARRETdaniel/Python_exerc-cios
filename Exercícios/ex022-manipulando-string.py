# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
texto = str(input('Digite seu nome completo: ')).strip() # strip eliminate the spaces from the biginner and end.
print('\nTudo em Minúsculas: \n{}'.format(texto.lower()))
print('Tudo em Maiúsculas: \n{}'.format(texto.upper()))
separado = texto.split()
junto = ''.join(separado)
print('Número de letras (sem espaços): {}'.format(len(junto)))
print('O primeiro nome ({}) tem {} letras'.format(
    separado[0], len(separado[0])))

