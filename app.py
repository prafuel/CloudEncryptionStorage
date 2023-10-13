from flask import *
import os
from datetime import datetime
from random import randint

# Local Modules
from src.encrypt import generate_key,load_key,encrypt_file,decrypt_file

key_history = "/home/version/Desktop/cc/src/keys/key_history.txt"

app = Flask("__name__",static_folder="static")

app.config['JSON_FILE'] = "/home/version/Desktop/cc/src/json_key"
app.config['KEY_FILE'] = "/home/version/Desktop/cc/src/keys/"
app.config['INPUT_FILE'] = "/home/version/Desktop/cc/original/"

@app.route("/",methods=['GET','POST'])
def index() :
    if request.method == 'POST':
        uploaded_files = {}

        # Check if a file was uploaded with the name 'jsonFile'
        if 'jsonFile' in request.files:
            json_file = request.files['jsonFile']
            if json_file:
                json_file.save(os.path.join(app.config['JSON_FILE'], "southern-branch-377015.json"))
                uploaded_files['jsonFile'] = os.path.join(app.config['JSON_FILE'], "southern-branch-377015.json")

        # Check if a file was uploaded with the name 'keyFile'
        if 'keyFile' in request.files:
            key_file = request.files['keyFile']
            if key_file:
                key_file.save(os.path.join(app.config['KEY_FILE'], "encryption_key.key"))
                uploaded_files['keyFile'] = os.path.join(app.config['KEY_FILE'], "encryption_key.key")

                with open(key_history,"a") as k:
                    k.write(str(datetime.now())+ ", " + str(load_key("/home/version/Desktop/cc/src/keys/encryption_key.key")) + "\n")

        # Check if a file was uploaded with the name 'fileInput'
        if "fileInput" in request.files:
            fileInput = request.files['fileInput']
            if fileInput:
                fileInput.save(os.path.join(app.config['INPUT_FILE'], fileInput.filename))
                uploaded_files['fileInput'] = os.path.join(app.config['INPUT_FILE'], fileInput.filename)

        return render_template("index.html")

    return render_template("index.html")

@app.route("/keys/",methods=["GET"])
def viewKey():
    key = None
    try:
        key_file = "/home/version/Desktop/cc/src/keys/encryption_key.key"
        key = load_key(key_file)
    except:
        pass
    return key
        

@app.route("/download/current_key/",methods=["GET"])
def download_key():
    try:
        # New Key
        key_file = "/home/version/Desktop/cc/src/keys/encryption_key.key"
        key = load_key(key_file)

        with open(key_history,"a") as k:
            k.write(str(datetime.now())+ ", " + str(key) + "\n")
        return send_file(key_file, as_attachment=True)
    except:
        return redirect("/download/create_key/")

@app.route("/download/create_key/",methods=["GET"])
def create_new():
    key_file = f"/home/version/Desktop/cc/#test/generated_keys/{str(randint(1,100000))}.key"
    key = generate_key(key_file)

    with open(key_history,"a") as k:
        k.write(str(datetime.now())+ ", " + str(key) + "\n")
    return send_file(key_file, as_attachment=True)
    

@app.route("/encrypt",methods=['GET','POST'])
def encrypt():
    if request.method == "POST":
        uploaded_files = {}

        if "encryptFile" in request.files:
            encryptFile = request.files["encryptFile"]
            if encryptFile:
                encryptFile.save(os.path.join(app.config['INPUT_FILE'], encryptFile.filename))
                uploaded_files['INPUT_FILE'] = os.path.join(app.config['INPUT_FILE'], encryptFile.filename)

                key = load_key("src/keys/encryption_key.key")
                # print(key)
                try:
                    encrypt_file(key,f"original/{encryptFile.filename}",f"#test/Encrypted/encrypted_{encryptFile.filename}")
                    return send_file(f"#test/Encrypted/encrypted_{encryptFile.filename}", as_attachment=True)
                except:
                    pass

    return render_template("encrypt.html")

@app.route("/decrypt",methods=['GET','POST'])
def decrypt():
    if request.method == "POST":
        uploaded_files = {}

        if "decryptFile" in request.files:
            decryptFile = request.files["decryptFile"]
            if decryptFile:
                decryptFile.save(os.path.join(app.config['INPUT_FILE'], decryptFile.filename))
                uploaded_files['INPUT_FILE'] = os.path.join(app.config['INPUT_FILE'], decryptFile.filename)

                key = load_key("src/keys/encryption_key.key")
                # print(key)
                try:
                    decrypt_file(key,f"original/{decryptFile.filename}",f"#test/Decrypted/decrypted_{decryptFile.filename}")
                    return send_file(f"#test/Decrypted/decrypted_{decryptFile.filename}",as_attachment=True)
                except:
                    return "Uploaded File Format is Not supported"

    return render_template("decrypt.html")

@app.route('/history',methods=["GET"])
def history():
    keyList = []
    with open(key_history,"r") as keys:
        for key in keys:
            keyList.append(key.strip())
    return keyList


if __name__ == "__main__" :
    app.run(debug=True, port=8080)