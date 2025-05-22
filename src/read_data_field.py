# le os campos do arquivo
def read_field(file):
    """
    Reads a field from the given file.
    :param file: The file to read from.
    :return: The field read from the file.
    """
    field = ''
    char = file.read(1)
    
    while char and char != '|':
        field += char
        char = file.read(1)
    return field

with open('src/output/global_output.txt', 'r', encoding='utf-8') as file:
    
    field = read_field(file)
    count = 0
    while field != '':
        
        print(f'Campo #{count}: {field}')
        count += 1
        field = read_field(file)