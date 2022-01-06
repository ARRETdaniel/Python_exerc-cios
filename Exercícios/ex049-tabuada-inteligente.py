# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('\nSmart Tabuada')

num = int(input('Informe um número para exibir sua tabuada: '))

print('{:-^14}'.format(num))

for count in range(1, 11):
    print(' {} x {:<2} = {}'.format(num, count, num * count))
