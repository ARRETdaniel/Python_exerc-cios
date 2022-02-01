"""
Desafio 114

Problema: Crie um código em Python que teste se o site Pudim está acessível pelo
          computador usado.

Resolução do problema:
"""
# Necessário instalar a biblioteca "requests" para importação
import requests
import urllib.request
import urllib

try:
    # A variável "response" recebe o objeto Response gerado pela requisição de metodo GET
    url = 'https://twitter.com/'
    response = requests.get(url)

    print(f'\n\33[32m{" CONEXÃO REALIZADA ":-^43}')
    print('Parece que você CONSEGUIU entrar no site...')
    print(f'URL: {url}'.center(43))
    print('-' * 43 + '\33[m')
except requests.ConnectionError:  # <-- As exceções de conexão são herdados dessa classe na lib requests
    print(f'\n\33[31m{" ERRO ":-^47}')
    print(
        f'Parece que você NÃO CONSEGUIU entrar no site...\n{"Tente mais tarde!".center(45)}')
    print('-' * 47 + '\33[m')


try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('O site não está acessivel no momento')
else:
    print(f'Consegui acessar o site com suceso')
    # print(site.read())
