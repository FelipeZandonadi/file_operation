from sys import argv

''' Função auxiliar que lê registros no formato gerado pelo escreve_registros.py'''
def leia_reg(arq) -> str:
        tam = int.from_bytes(arq.read(2))
        if tam > 0:
            s = arq.read(tam)
            return s.decode()
        return ''

''' Função principal '''
def main() -> None:
    try:
        # verifica se o nome do arquivo foi passado pela linha de comando
        if (len(argv) > 1):
            nomeArq = argv[1]
        else:
            nomeArq = input('Digite o nome do arquivo a ser aberto: ')
        arq = open(nomeArq, 'rb')
        contaReg = 1
        buffer = leia_reg(arq)
        while buffer:
            print(f"\nRegistro #{contaReg} (Tam = {len(buffer)}):")
            contaCampo = 1
            for campo in buffer.split(sep='|'):
                if campo:
                    print(f"Campo #{contaCampo}: {campo}")
                    contaCampo += 1
            contaReg += 1
            buffer = leia_reg(arq)
        print()
        arq.close()
    # OSError é a classe geral de erros que podem ocorrer na manipulação do arquivo
    except OSError as e:
        print(f'Erro: {e}')
    

if __name__ == '__main__':
    main()