
from cryptography.fernet import Fernet

# Generate and load the encryption key
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key(key_file):
    return open(key_file, 'rb').read()

if __name__ == "__main__":
    key_file = "/home/version/Desktop/cc/src/keys/encryption_key.key"
    key = generate_key(key_file)
    print(key)