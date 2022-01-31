"""
Desafio 111

Problema: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
          moeda e dado.

          Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para
          o primeiro pacote e mantenha tudo funcionando.

Resolução do problema:
"""
from ex111.utilidadescev import moeda, dado
from ex111.utilidadescev import dado

p = float(input('Digite o preço: R$'))
moeda.resumo(p)
