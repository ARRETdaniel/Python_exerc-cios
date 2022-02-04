def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaString(msg):
    while True:
        try:
            name = input(msg)
            # if ((len(name) > 2) & (name.isalpha())):
            if (name.replace(' ', '').isalpha()):
                name
                # break
            else:
                raise TypeError

        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar.\033[m')
            return ''
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um nome com apenas str.\033[m')
            continue

        else:
            return name


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc
