# Nosso time de futebol terminou o campeonato. O resultado de cada correspondência é semelhante a "x: y".
# Os resultados de todas as partidas são registrados na coleção.


# Escreva uma função que leve essa arrecadação e conte os pontos da nossa
# equipe no campeonato. Regras para contagem de pontos para cada partida:
limpa = '\033[m'
azul = '\033[1;34m'

def pontos_time(points, totPoints):

    totPoints_values = list(points.values())

    for i in range(0, len(totPoints_values)):
        if (totPoints_values[i][0] > totPoints_values[i][1]):
            totPoints += 3
        elif (totPoints_values[i][0] == totPoints_values[i][1]):
            totPoints += 1
        # (x < y):
        else:
            totPoints += 0
    print(f'Total de pontos da equipe no campeonato: {azul}{totPoints}{limpa}')


# - há 10 partidas no campeonato
points = {('partida1'): (4, 1),
          ('partida2'): (3, 1),
          ('partida3'): (2, 1),
          ('partida4'): (1, 5),
          ('partida5'): (1, 1),
          ('partida6'): (0, 1),
          ('partida7'): (0, 0),
          ('partida8'): (2, 1),
          ('partida9'): (0, 0),
          ('partida10'): (0, 0)}

# pontos atual da equipe
totPoints = 0

pontos_time(points, totPoints)
