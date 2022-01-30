"""
Desafio 109

Problema: Modifique as funções que foram criadas no desafio 107 para que elas
          aceitem um paràmetro a mais, informando se o valor retornado por elas
          vai ou não ser formatado pela função moeda(), desenvolvida na aula 108.

Resolução do problema:
"""
from ex109 import moeda

value = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(value)} é {(moeda.metade(value, True))}')
print(f'O dobro de {moeda.moeda(value)} é {(moeda.dobro(value, True))}')
print(f'Aumentando 10%, temos {(moeda.aumentar(value, 10, True))}')
print(f'Reduzindo 13%, temos {(moeda.diminuir(value, 13, True))}')
