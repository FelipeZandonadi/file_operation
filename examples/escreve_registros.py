from sys import argv

''' A lista `mensagens` contém as strings que serão usadas pela função
    input na leitura dos campos '''
mensagens = [
    '                                   Nome: ',
    '                               Endereco: ',
    '                                 Cidade: ',
    '                                 Estado: ',
    '                                    CEP: '
]

''' Função auxiliar que concatena o campo no buffer junto com o | '''
def concatena_campo(buffer: str, campo: str) -> str:
    return buffer + campo + '|'
    

def main() -> None:
    try:
        if (len(argv) > 1):
            nomeArq = argv[1]
        else:
            nomeArq = input('Digite o nome do arquivo a ser aberto: ')
        
        with open(nomeArq, 'wb') as arq:
            campo = input('Digite o sobrenome ou <ENTER> para sair: ')
            while campo:
                buffer = concatena_campo('', campo)
                for m in mensagens:
                    campo = input(m)
                    buffer = concatena_campo(buffer, campo)
                # caracteres especiais vão ocupar mais de um byte depois de decodificados, 
                # por isso precisa decodificar a string antes de calcular o tamanho 
                buffer = buffer.encode()
                lenBuffer = len(buffer)
                arq.write(lenBuffer.to_bytes(2))
                arq.write(buffer)
                campo = input('Digite o sobrenome ou <ENTER> para sair: ')
    # OSError é a classe geral de erros que podem ocorrer na manipulação do arquivo
    except OSError as e:
        print(f'Erro: {e}')
    

if __name__ == '__main__':
    main()