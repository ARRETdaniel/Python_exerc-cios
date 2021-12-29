# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print('Quantas vezes a letra "A" aparece? {}'.format(frase.count('a')))
print('Em que posição ela aparece a primeira vez? {}'.format(frase.find('a') + 1))
print('Em que posição ela aparece a última vez? {}'.format(frase.rfind('a') + 1)) # rfind find from right to left.
