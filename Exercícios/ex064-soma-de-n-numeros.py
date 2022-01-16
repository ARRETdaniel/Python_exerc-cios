# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
# o flag).
count = num = som = 0
print('\nA qualquer momento digite 999 para sair\n')
while num != 999:
    num = int(input('Digite o {}º número: '.format(num + 1)))
    if num != 999:
        som += num
        count += 1
if count == 0:
    print('\nNenhum número fornecido!')
elif count == 1:
    print('\nO único número fornecido foi {}'.format(som))
else:
    print('\n{} números foram fornecidos, a soma entre eles é {}'.format(count, som))
