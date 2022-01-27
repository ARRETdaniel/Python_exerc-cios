"""
Desafio 095

Problema: Aprimore o desafio 093 para que ele funcione com vários jogadores,
          incluindo um sistema de visualização de detalhes do aproveitamento
          de cada jogador.

Resolução do problema:
"""
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;35m'       # 6 - branco
     )

cor = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'title': '\033[1;30m',
    'danger': '\033[7;31m'
}

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\nInforme a opção corretamente... [S/N]')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for key, value in enumerate(time):
    print(f'{key:>3} ', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(
        input('Mostrar dados de qual jogador?  DIGITE COD \n (999 para parar).'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Nao ha jogador com o codigo: {busca}')
    else:
        print(
            f'--- LEVANTAMENTO DO JOGADOR: {cor["azul"]}  {time[busca]["nome"]} {cor["limpa"]}')
        for partida, gols in enumerate(time[busca]['gols']):
            print(f'No jogo {partida+1} fez {gols} gols.')
print('-='*30)
print('----- PROGRAMA ENCERRADO -----')

'''
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')


print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'    ==> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
'''
