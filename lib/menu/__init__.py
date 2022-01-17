# // Lê a resposta do user e verifica se o type está correto (int).
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Tente digitar um opção válida.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usúario preferiu não digitar uma opção.\033[m')
            return 3
            break
        else:
            return n
            break


def linha(tam=40):  # // Cria uma linha com o tamanho que deseja, padrão 40.
    return '\033[m\033[1m-\033[m' * tam


def cabeçalho(txt='.'):  # // Forma um cabeçalho para destaque.
    print(linha())
    print(f'\033[34m{txt.center(40)}\033[m')
    print(linha())


def menu(opc):  # // Menu com opções personalizadas em forma de lista.
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for c in opc:
        print(f'\033[33m{cont} \033[m- \033[34m{c.capitalize()}\033[m')
        cont += 1
    print(linha())
    user = leiaInt('\033[33mSua opção:\033[m\033[34m ')
    print('\033[m')
    return user
