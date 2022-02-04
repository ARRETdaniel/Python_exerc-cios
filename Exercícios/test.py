from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

n = "Compan2y"

if n.isalpha():
    # n = str(input(n))
    print('entrou')
else:
    print("nao entrou")


if not n.replace(' ', '').isalpha():
  print('Bad name!')
else:
  print('Good name!')


nome = leiaString('Nome: ')
