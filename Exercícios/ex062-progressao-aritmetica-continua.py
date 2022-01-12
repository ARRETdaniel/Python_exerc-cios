# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
exibidos = 0
limite = 0
c = 1
continuar = 10

while continuar != 0:

    exibidos = exibidos + continuar
    while c <= exibidos:
        print(primeiro + (c - 1) * razao, end=', ')
        c += 1

    print('pausa')
    continuar = int(input('Deseja exibir mais quantos termos? '))
    
print('Programa finalizado')
