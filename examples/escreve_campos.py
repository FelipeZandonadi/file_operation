from sys import argv
from mockup_generator import mockup_user_generator

def main() -> None:
    # se o nome do arquivo a ser aberto foi passado pela linha de comando, use-o
    # caso contrário, leia o nome do arquivo
    if (len(argv) > 1):
        nomeArq = argv[1]
    else:
        nomeArq = input('Digite o nome do arquivo a ser aberto: ')
    try:
        with open(nomeArq, 'w', encoding='utf-8') as arq:
            users = mockup_user_generator(500)
            for user in users:
                first_name = user['first_name']
                last_name = user['last_name']
                street_name = user['street_name']
                street_number = user['street_number']
                city = user['city']
                state = user['state']
                postcode = user['postcode']
                arq.write(f"{last_name}|{first_name}|{street_name} {street_number}|{city}|{state}|{postcode}|")

    except OSError as e:
        print(f'Erro: {e}')
    

if __name__ == '__main__':
    main()