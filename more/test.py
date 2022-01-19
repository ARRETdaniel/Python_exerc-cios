def retorne_seculo(ano):

    # valores negativos nao sao levados em conta
    if (ano <= 0):
        print("Ano {} nao valido").format(ano)

    # O primeiro século vai do ano 1 até e incluindo o ano 100
    elif (ano <= 100):
        print("Seculo 1")

    # resto da divisao igual a 0
    elif ((ano % 100) == 0):
      print(ano // 100, "Seculo")

    # se a divisao tiver resto Ex: ano 1705 % 100 = 5,
    #  (1705 // 100) + 1 = 18
    else:
      print(((ano // 100) + 1), "Seculo")

# ano
ano = [1, 101, 1705, 1900, 1601, 2000, 2001]
for i in ano:
    retorne_seculo(i)
