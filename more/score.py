# Nosso time de futebol terminou o campeonato. O resultado de cada correspondência é semelhante a "x: y".
# Os resultados de todas as partidas são registrados na coleção.


# Escreva uma função que leve essa arrecadação e conte os pontos da nossa
# equipe no campeonato. Regras para contagem de pontos para cada partida:
def pontos_time(pontos, totPoints):

    pontosNew = list(pontos.values())

    for i in range(0, len(pontosNew)):

        if (pontosNew[i][0] > pontosNew[i][1]):
            totPoints += 3

        elif (pontosNew[i][0] == pontosNew[i][1]):
            totPoints += 1
        # (x < y):
        else:
            totPoints += 0
    print(totPoints)


# - há 10 partidas no campeonato
pontos = {('partida1'): (4, 1),
          ('partida2'): (3, 1),
          ('partida3'): (2, 1),  # 9
          ('partida4'): (1, 5),
          ('partida5'): (1, 1),  # 10
          ('partida6'): (0, 1),
          ('partida7'): (0, 0),  # 11
          ('partida8'): (2, 1),  # 14
          ('partida9'): (0, 0),
          ('partida10'): (0, 0)}  # 16

# pontos atual da equipe
totPoints = 0

#pontos[('Brazil', 'Agentina')]
# print(pontos)


print(list(pontos.values()))
pontosNew = list(pontos.values())
print('---')
print(pontosNew[7][0])
print(pontosNew)
#print(pontos.get('nossaEquipe', 'outroTime')[1])


pontos_time(pontos, totPoints)
