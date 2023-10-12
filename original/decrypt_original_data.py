
import os
from cryptography import fernet

key = open("src/keys/encryption_key.key", "rb").read()
print(key)

# Decrypt a file

def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)


folder = os.listdir("./original/")
for file in folder:
    if "txt" in file:
        print(file)
        file = f"./original/{file}"
        decrypt_file(key,file,file)
