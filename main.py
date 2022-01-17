# Importações
from lib.menu import *
from lib.arquivo import *
from time import sleep

# Verificação e criação de arquivo
arq = "./cadastrados.txt"
if not verificarArquivo(arq):
    criarArquivo(arq)

# Título
f = '\033[1mSISTEMA DE CADASTRO\033[m'
print(f.center(47))

# Menu do usúario
while True:
    resposta = menu(['Cadastrar um usúario',
                     'Visualizar lista de cadastros',
                     'Sair do sistema'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        while True:
            try:
                nome = str(input('\033[33mNome:\033[m\033[34m '))
                idade = int(input('\033[33mIdade:\033[m\033[34m '))
            except (ValueError, TypeError, KeyboardInterrupt):
                print('\033[31mERRO: O dado inserido é inválido.')
            else:
                cadastrar(arq, nome, idade)
                break
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('\033[33mSaindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO: Resposta inválida! Tente novamente.\033[m')
    sleep(2)
