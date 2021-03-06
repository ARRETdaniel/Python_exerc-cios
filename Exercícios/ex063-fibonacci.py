# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
print('Sequência \033[34mFibonacci\033[m')

n = int(input('Digite quantos números da sequência Fibonacci você quer exibir: '))

n1 = 0
n2 = 1

if n == 0:
    print('Nenhum número para exibir!')
elif n == 1:
    print('O primeiro número da sequência é {}'.format(n))
elif n >= 2:
    print('Os {} primeiros números da sequência são: '.format(n))
    print('{}, {}'.format(n1, n2), end=', ')
    cont = 2
    while cont < n:
        n3 = n1 + n2
        print('{}, '.format(n3), end='')
        n1 = n2
        n2 = n3
        cont += 1
    print('FIM')
else:
    print('\033[31mNúmero inválido!')
