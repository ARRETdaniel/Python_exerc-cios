"""
Desafio 101

Problema: Crie um programa que tenha uma função chamada voto() que vai receber
          como parâmetro o ano de nascimento de uma pessoa, retornando um valor
          literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
          nas eleições.

Resolução do problema:
"""


def calc_idade(nascimento):
    from datetime import date
    return date.today().year - nascimento


def voto(ano_nasc):  # Função responsável por verificar se pode ou não votar
    """[summary]

    Args:
        ano_nasc ([type]): [description]

    Returns:
        [type]: [description]
    """
    idade = calc_idade(ano_nasc)
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:# idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano_nascimento = 2000  # int(input('Informe o ano de seu nascimento: '))

print(voto(ano_nascimento))
# Argumentos passados para a função voto():
#           ano_nascimento = ano informado pelo usuário;
#           calc_idade = função para calcular idade do usuário.
