from mockup_generator import mockup_user_generator

def add_value_to_file(value, file):
    file.write(f"{value}|")

def main():
    users = mockup_user_generator(50)
    
    with open('output/global_output.txt', 'w', encoding='utf-8') as file:
        for user in users:
            add_value_to_file(user['first_name'], file)
            add_value_to_file(user['last_name'], file)
            add_value_to_file(f"{user['street_name']} {user['street_number']}", file)
            add_value_to_file(user['city'], file)
            add_value_to_file(user['state'], file)
            add_value_to_file(user['postcode'], file)
    
if __name__ == "__main__":
    main()
