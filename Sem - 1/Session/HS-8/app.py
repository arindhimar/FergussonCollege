from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("select * from todoapitb")
    data = cur.fetchall()
    # print(data)
    return render_template("todo.html",todos=data)

@app.route('/add', methods=['POST'])
def add_todo():
    # print(request.form)
    title = request.form["name"]
    desc = request.form["desc"]
    
    cur = mysql.connection.cursor()
    cur.execute(f"insert into todoapitb(todoTitle,todoDescription) values('{title}','{desc}')")
    cur.connection.commit()
    return redirect("/")
    

@app.route("/delete/<int:todoid>",)
def delelte_todo(todoid):
    print(todoid)
    return redirect("/")


@app.route("/update/<int:todoid>",methods=["GET","POST"])
def edit_todo(todoid):
    cur = mysql.connection.cursor()
    
    if request.method == "POST":
        title = request.form["name"]
        desc = request.form["desc"]
        cur.execute(f"update todoapitb set todoTitle='{title}' , todoDescription='{desc}' where todoid={todoid}")
        cur.connection.commit()
        return redirect ("/")
    
    cur.execute(f"select * from todoapitb where todoid={todoid}")
    data = cur.fetchone()
    return render_template("todo.html",todo=data)

if __name__ == "__main__":
    app.run(debug=True)