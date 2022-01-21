# Exercício Python 080: Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []

for c in range(1, 6):
    num = (int(input('Digite um valor: ')))
    if len(lista) == 0:
        print(f'Valor {num} adicionado ao final da lista')
        lista.append(num)
    else:
        for i in range(0, len(lista)):
            if num <= lista[i]:
                print(f'Valor {num} adicionado na posição {i} da lista')
                lista.insert(i, num)
                break
            elif i == (len(lista) - 1):
                print(f'Valor {num} adicionado ao final da lista')
                lista.append(num)

print(f'Você digitou {lista}')

otherList = []
# Video aula solution:
for c in range(0, 5):
    num = (int(input('Digite um: ')))
    if c == 0 or num > otherList[-1]:
        otherList.append(num)
        print(f'Valor {num} adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(otherList):
            if num <= otherList[pos]:
                otherList.insert(pos, num)
                print(f'Valor {num} adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Você digitou {otherList}')
