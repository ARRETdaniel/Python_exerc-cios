def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, perc=0, formato=False):
    res = n + (n * (perc/100))
    return res if formato is False else moeda(res)


def diminuir(n=0, perc=0, formato=False):
    res = n - (n * (perc/100))
    return res if formato is False else moeda(res)


def moeda(n=0, moeda ='R$ '):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(preco=0, perc=10, taxa=5):
    dic = {'Preço analisado:': moeda(preco), 'Dobro do preço:': dobro(preco, True),
           'Metade do preço:': metade(preco, True), f'{perc}% de aumento:': aumentar(preco, perc, True),
           f'{taxa}% de redução:': diminuir(preco, taxa, True)}
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    for k, v in dic.items():
        print(f'{k:<20} {v:<5}')
    print('-' * 30)
