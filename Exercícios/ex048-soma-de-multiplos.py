# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
print('Soma dos números ímpares múltiplos de 3 entre 1 e 500')
s = 0
total = 0

for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        total += 1
print('A soma dos {} numeros é {}'.format(total, s))


s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        s = s + c
print('A soma de todos os {} numeros solicitados é {}'.format(count, s))
