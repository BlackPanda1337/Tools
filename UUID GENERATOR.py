import secrets
import string

def generate_master_key(length):
    characters = string.ascii_letters + string.digits
    master_key = ''.join(secrets.choice(characters) for _ in range(length))
    return master_key

master_key = generate_master_key(64)
print(master_key)