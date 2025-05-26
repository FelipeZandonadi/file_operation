import io
from sys import argv

def leia_campo(arq: io.TextIOWrapper) -> str:
    campo = ''
    c = arq.read(1)
    # o método read retornará uma string vazia no EOF
    # strings vazias '' retornam False no contexto do while
    while c and c != '|':
        campo += c
        c = arq.read(1)
    return campo


def main() -> None:
    # se o nome do arquivo a ser aberto foi passado pela linha de comando, use-o
    # caso contrário, leia o nome do arquivo
    if (len(argv) > 1):
        nomeArq = argv[1]
    else:
        nomeArq = input('Digite o nome do arquivo a ser aberto: ')
    try:
        with open(nomeArq, 'r') as arq:
            contaCampo = 1
            campo = leia_campo(arq)
            while campo:
                print(f'\tCampo #{contaCampo}: {campo}')
                contaCampo += 1
                campo = leia_campo(arq)
    except OSError as e:
        print(f'Erro: {e}')
    

if __name__ == '__main__':
    main()