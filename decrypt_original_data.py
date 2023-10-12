
import os
from src.encrypt import decrypt_file,encrypt_file

key = open("src/keys/encryption_key.key", "rb").read()
print(key)


folder = os.listdir("./original/")
for file in folder:
    if "txt" in file:
        print(file)
        file = f"./original/{file}"
        decrypt_file(key,file,file)
