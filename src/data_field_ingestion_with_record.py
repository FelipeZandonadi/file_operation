from mockup_generator import mockup_user_generator

def add_value_to_file(value, file):
    len_value = len(value) + 1
    # +1 for the '|' character
    bin_len_value = len_value.to_bytes(2)
    file.write(bin_len_value+value.encode('utf-8'))

def main():
    with open('output/global_output.txt', 'wb') as file:
        users = mockup_user_generator(3)
        for user in users:
            add_value_to_file(f'{user['first_name']}|{user['last_name']}|{user['street_name']}|{user['street_number']}|{user['city']}|{user['state']}|{user['postcode']}|', file)

if __name__ == "__main__":
    main()