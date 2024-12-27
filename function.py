def create_account(account_details):
    try:
        with open('data/accounts.txt', 'a') as file:
            file.write(account_details + "\n")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
    
def add_transaction(transaction_details):
    try:
        with open('data/transactions.txt', 'a') as file:
            file.write(transaction_details + "\n")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    

def custom_hash(password, salt="securePassword"):
    # Convert password and salt into a list of ASCII values
    password_ascii = [ord(char) for char in password]
    salt_ascii = [ord(char) for char in salt]

    # Combine ASCII values with some basic transformations
    combined = [(p + s) % 256 for p, s in zip(password_ascii, salt_ascii)]
    
    # Add padding if password length < salt length
    if len(password) < len(salt):
        combined.extend([ord(salt[i]) for i in range(len(password), len(salt))])
    
    # Convert back to a hex string
    hashed = ''.join(f'{num:02x}' for num in combined)
    return hashed

def check_credentials(account_number,password):
    data = file_to_dict("data/accounts.txt")
    if account_number in data and data[account_number][1] == password:
        return data
    else:
        return False

def file_to_dict(filename):
    result_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by commas and strip whitespace
                parts = line.strip().split(',')
                if len(parts) >= 4:  # Ensure there are enough parts
                    key = parts[0]
                    value = parts[1:4]  # Take the next three elements as the list
                    result_dict[key] = value
            return result_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def dict_to_file(data_dict, filename = "data/accounts.txt"):
    try:
        with open(filename, 'w') as file:
            for key, value in data_dict.items():
                # Combine key and list values into a single comma-separated string
                val = map(str, value)
                line = key + ',' + ','.join(val) + '\n'
                file.write(line)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False