from flask import *
import os
from datetime import datetime
from random import randint

# Local Modules
from src.encrypt import generate_key,load_key

key_history = "/home/version/Desktop/cc/src/keys/key_history.txt"

app = Flask("__name__")

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

@app.route("/keys",methods=["GET"])
def viewKey():
    keyList = []
    with open(key_history,"r") as keys:
        for key in keys:
            keyList.append(key.strip())
    return keyList

@app.route("/download/current_key",methods=["GET"])
def download_key():
    # New Key
    key_file = "/home/version/Desktop/cc/src/keys/encryption_key.key"
    key = load_key(key_file)

    # with open(key_history,"a") as k:
    #     k.write(str(datetime.now())+ ", " + str(key) + "\n")
    return send_file(key_file, as_attachment=True)

@app.route("/download/create_key",methods=["GET"])
def create_new():
    key_file = f"/home/version/Desktop/cc/#test/generated_keys/{str(randint(1,100000))}.key"
    key = generate_key(key_file)

    with open(key_history,"a") as k:
        k.write(str(datetime.now())+ ", " + str(key) + "\n")
    return send_file(key_file, as_attachment=True)
    

@app.route("/encrypt",methods=['GET'])
def encrypt():
    return "Encrypt your File Here"

if __name__ == "__main__" :
    app.run(debug=True, port=8000)