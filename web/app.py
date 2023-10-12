from flask import *

app = Flask("__name__")

@app.route("/",method=['GET','POST'])
def index() :

    if request.method == 'POST':
        pass
        # Working HERE.... on UPLOADIN SECTION

    return render_template("index.html")

if __name__ == "__main__" :
    app.run(debug=True, port=8000)