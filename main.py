from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='')
variable=0
array = []

@app.route("/")
def mano_funkcija():
    return ("Labas")

@app.route("/test")
def test_route():
    return render_template('./index.html',var=plus_one())

@app.route("/debug")
def plus_one():
    global variable
    variable = variable +1
    return str(variable)

@app.route("/notes",methods=["GET","POST"])
def notes():
    if(request.method == "POST"):
        global array
        args = request.form.get("note2")
        if (args):
            array.append(args)
            print(array)
        return render_template('./notes.html',note=array)
    else:
        return render_template('./notes.html',note=array)


if __name__=="__main__":
    app.run(debug="true")


