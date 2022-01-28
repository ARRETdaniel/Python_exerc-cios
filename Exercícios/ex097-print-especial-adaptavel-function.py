"""
Desafio 097

Problema: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
          como parâmetro e mostre uma mensagem com o tamanho adaptável.

          Ex: escreva('Olá, Mundo!')

          Saída:
                -------------
                 Olá, Mundo!
                -------------

Resolução do problema:
"""


# Função para imprimir mensagens dentro de cabeçalho com bordas
def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}  ')
    print('-' * (len(mensagem) + 4))

#resposta do Gustavo
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)  # pra ficar com 2 ~ na esquerda e 2 ~ na direita sobrando
    print(f'  {msg}')
    print('~' * tam)


#programa principal
escreva('Gustavo Guanabara')
escreva('Curso em Python no YouTube')
escreva('CeV')
