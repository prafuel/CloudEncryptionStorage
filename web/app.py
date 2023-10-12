from flask import *
import os

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
                json_file.save(os.path.join(app.config['JSON_FILE'], json_file.filename))
                uploaded_files['jsonFile'] = os.path.join(app.config['JSON_FILE'], json_file.filename)

        # Check if a file was uploaded with the name 'keyFile'
        if 'keyFile' in request.files:
            key_file = request.files['keyFile']
            if key_file:
                key_file.save(os.path.join(app.config['KEY_FILE'], "encryption_key.key"))
                uploaded_files['keyFile'] = os.path.join(app.config['KEY_FILE'], "encryption_key.key")
        
        # Check if a file was uploaded with the name 'fileInput'
        if "fileInput" in request.files:
            fileInput = request.files['fileInput']
            if fileInput:
                fileInput.save(os.path.join(app.config['INPUT_FILE'], fileInput.filename))
                uploaded_files['fileInput'] = os.path.join(app.config['INPUT_FILE'], fileInput.filename)

        return render_template("index.html")

    return render_template("index.html")

@app.route("/encrypt",methods=['GET'])
def encrypt():
    return "Encrypt your File Here"

if __name__ == "__main__" :
    app.run(debug=True, port=8000)