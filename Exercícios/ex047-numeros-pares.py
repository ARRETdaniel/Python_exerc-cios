# Exercício Python 047: Crie um programa que mostre na tela
# todos os números pares que estão no intervalo entre 1 e 50.

print('\033[1;30mNúmeros pares entre 1 e 50:\033[30m')
for count in range(1, 51):  # range(2, 51, 2): range(2, 51, 2), que é mais otmizado

    if count % 2 == 0:
        print(count, end=' ')
print('Fim')


for count in range(2, 51, 2):  # range(2, 51, 2): range(2, 51, 2), que é mais otmizado
    print(count, end=' ')
print('Fim')
