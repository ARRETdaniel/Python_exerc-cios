"""
Desafio 106

Problema: Faça um mini-sistema que utilize o interative Help do Python. O usuário
          vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
          a palavra 'FIM' o programa se encerrará.

          Obs: Use cores.

Resolução do problema:
"""
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;35m'       # 6 - branco
     )


def header_pyhelp():
    """
    -> Imprime na tela o cabeçalho do PyHelp
    :return: Não possui retorno
    """
    print('\33[30;42m-' * 35 +
          f'\n{"SISTEMA DE AJUDA PyHelp":^35}\n' + '-' * 35)


def header_search_pyhelp(search):
    """
    -> Imprime na tela o cabeçalho responsivo do manual
    :param search: Parâmetro para receber a palavra pesquisada pelo usuário
    :return: Sem retorno
    """
    header = f'Acessando o manual do comando "{search}"'
    print('\33[30;44m~' * (len(header) + 4))
    print(f'  {header}  ')
    print('~' * (len(header) + 4))


def pyhelp(search):
    """
    -> Realiza uma pesquisa na função/biblioteca escolhida e imprime sua documentação.
    :param search: Parâmetro para receber a palavra pesquisada pelo usuário.
    :return: Retorna a documentação da função/biblioteca pesquisada.
    """
    header_search_pyhelp(search)
    print('\33[37;40m', end='')
    return help(search)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)


while True:
    header_pyhelp()
    pesquisa = input('\33[mFunção ou Biblioteca >>> ').strip().lower()

    if pesquisa.upper() == 'FIM':
        print('\33[30;41m=' * 20 + f'\n{"FINALIZADO":^20}\n' + '=' * 20)
        break

    pyhelp(pesquisa)

'''
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
'''
