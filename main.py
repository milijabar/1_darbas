from flask import Flask, render_template, request
import sqlite3
connection=sqlite3.connect("./NotesDatabase.db")


app = Flask(__name__,static_url_path='')
variable=0
array = []
res=[]


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
            insert_into_db(args)
            print(array)
        return render_template('./notes.html',note=array)
    else:
        return render_template('./notes.html',note=array)


@app.route("/registracija",methods=["GET","POST"])
def registracija():
    return render_template('./registracija.html')
        

def createDB():

    global connection
    cursor=connection.cursor()
    createTableString = """CREATE TABLE IF NOT EXISTS Sheets (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )"""

    createNotesTableString = """CREATE TABLE IF NOT EXISTS Notes (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        SheetId INTEGER NOT NULL,
        Header TEXT
        Text TEXT,
        FOREIGN KEY (SheetId) REFERENCES Sheets(Id)
    )"""
    cursor.execute(createTableString)
    cursor.execute(createNotesTableString)

def insert_into_db(note):
    global connection
    connection=sqlite3.connect("./NotesDatabase.db")
    queryString="""
        INSERT INTO Sheets (Name) VALUES (?) 
    """
    cur=connection.cursor()
    cur.execute(queryString,(note,))
    connection.commit()

def select_from_db():
    connection=sqlite3.connect("./NotesDatabase.db")
    queryString="""
        SELECT name FROM Sheets
    """
    cur=connection.cursor()
    array = cur.execute(queryString).fetchall()
    print(array)

if __name__=="__main__":
    createDB()
    app.run(debug="true")

