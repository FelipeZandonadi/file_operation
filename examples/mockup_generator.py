import requests

def mockup_user_generator(qty_users):
    """
    Generate a specified number of mockup users.
    Returns a list of dictionaries containing user data.
    Args:
        qty_users (int): The number of users to generate.
    Returns:
        list: A list of dictionaries containing user data.
    """
    
    users = []
    response = requests.get(f"https://randomuser.me/api/?results={qty_users}")
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
    for user in response.json()['results']:
        user_data = {
            'first_name': user['name']['first'],
            'last_name': user['name']['last'],
            'street_number': user['location']['street']['number'],
            'street_name': user['location']['street']['name'],
            'city': user['location']['city'],
            'state': user['location']['state'],
            'postcode': user['location']['postcode']
        }
        users.append(user_data)
    return users