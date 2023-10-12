
import os
from src.encrypt import generate_key,load_key,encrypt_file,decrypt_file
from src.googleDriveApi.drive import on_drive
from src.googleDriveApi.Download.download import download_file

if __name__ == "__main__":
    key_file = './src/keys/encryption_key.key'

    input_folder = './original'
    encrypted_folder = './Encrypted'
    decrypted_folder = './Decrypted'


    # Generating key
    if not os.path.exists(key_file):
        key = generate_key(key_file)
    else:
        key = load_key(key_file)
    
    # print(key)

    # Files to be encrypted 
    folder_path = "./original/"

    ''' file_names = os.listdir(folder_path)
    for name in file_names:
        file = f"{folder_path}{name}"
        # Encrypt Files 
        encrypt_file(key,file,file)

    # Save Encrypted Files on Google Cloud using Google Drive API
    JSON_KEY_FILE = "src/json_key/southern-branch-377015.json"
    for name in file_names:
        file = f"{folder_path}{name}"
        print(file)
        on_drive(JSON_KEY_FILE,file) '''


    JSON_KEY_FILE = "src/json_key/southern-branch-377015.json"
    with open("src/googleDriveApi/file_id.txt") as ids :
        for id in ids:
            print(id.split(":")[1].strip())
            file_id = id.split(":")[1].strip()
            # Downloading Encrypted Data 
            filename = id.split(":")[0].strip()
            download_file(file_id=file_id, JSON_KEY_FILE=JSON_KEY_FILE, file_name=filename)


    # Decrypt Files from Encrypted Folder
    decry_save_path = "./#test/Decrypted/"
    file_names = os.listdir("#test/Encrypted/")
    for name in file_names:
        file = f"#test/Encrypted/{name}"
        decry_file_path = f"{decry_save_path}{name}"
        # Decrypt Files 
        decrypt_file(key,file,decry_file_path)



