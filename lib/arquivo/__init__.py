# Importações
from lib.menu import cabeçalho


# // Abre o arquivo, caso não exista retorna False.
def verificarArquivo(name):
    try:
        a = open(name, 'rt')  # Tenta abrir o arquivo name, no modo leitura.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# // Cria o arquivo seguindo o bool da função "verificarArquivo".
def criarArquivo(name):
    # Escreve (wt) o arquivo name, e caso não exista, o cria (+).
    a = open(name, 'wt+')
    a.close()


def lerArquivo(name):  # // Lê o arquivo e mostra os dados dos cadastros.
    try:
        a = open(name, 'rt')
    except:
        print('\033[31mHouve um erro ao ler o arquivo.\033[m')
    else:
        cabeçalho('CADASTROS:')
        print('{:<30} {:>28}'.format(
            ('\033[1;33mNOME CADASTRADO\033[m'), ('\033[1;34mIDADE\033[m')))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(
                f'\033[33m{dado[0]:<30}\033[m \033[34m{dado[1]:>3} anos\033[m')
    finally:
        a.close()


def cadastrar(arq, nome, idade):  # // Cadastra no arquivo os dados inseridos.
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mNão foi possível abrir o arquivo.')
    else:
        try:
            a.write(f'\n{nome};{idade}')  # Escreve os dados no arquivo
        except:
            print('\033[31mHouve um erro no cadastro.\033[m')
        else:
            print(f'\033[32mCadastro de {nome} realizado com sucesso!')
            a.close()
