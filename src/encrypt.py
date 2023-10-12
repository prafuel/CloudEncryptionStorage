import os
from cryptography.fernet import Fernet

# Generate and load the encryption key
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key(key_file):
    return open(key_file, 'rb').read()

# Encrypt a file
def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Encrypt all files in a folder and its subfolders
def encrypt_all_files(key, input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            input_file = os.path.join(root, filename)
            output_file = os.path.join(output_folder, os.path.relpath(input_file, input_folder))
            encrypt_file(key, input_file, output_file)

# Decrypt all files in a folder and its subfolders
def decrypt_all_files(key, input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            input_file = os.path.join(root, filename)
            output_file = os.path.join(output_folder, os.path.relpath(input_file, input_folder))
            decrypt_file(key, input_file, output_file)

if __name__ == "__main__":

    key_file = './keys/encryption_key.key'
    input_folder = './original'
    encrypted_folder = './Encrypted'
    decrypted_folder = './Decrypted'

    # Generate or load the encryption key
    if not os.path.exists(key_file):
        key = generate_key(key_file)
    else:
        key = load_key(key_file)

    # Encrypt all files in the working folder
    encrypt_all_files(key, input_folder, encrypted_folder)

    # Decrypt all files in the working folder
    decrypt_all_files(key, encrypted_folder, decrypted_folder)
