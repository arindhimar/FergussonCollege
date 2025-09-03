from flask import Flask,redirect,render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route("/")
def get_todos():
    cur = mysql.connection.cursor()
    cur.execute("select * from todoapitb")
    data = cur.fetchall()
    # print(data)
    return render_template("todo.html",todos=data)

@app.route("/delete/<int:todoid>")
def delete_task(todoid):
    print(todoid)
    cur = mysql.connection.cursor()
    cur.execute(f"delete from todoapitb where todoid={todoid}")
    cur.connection.commit()
    return redirect("/")

@app.route("/add",methods=["POST"])
def add_task():
    # print(request.form)
    title = request.form["title"]
    desc = request.form["desc"]
    cur = mysql.connection.cursor()
    
    cur.execute(f"insert into todoapitb(todoTitle,todoDescription) values('{title}','{desc}')")
    cur.connection.commit()
    return redirect("/")

@app.route("/edit/<int:todoid>",methods=["GET","POST"])
def edit_task(todoid):
    cur = mysql.connection.cursor()
    if request.method=="POST":
        title = request.form["title"]
        desc = request.form["desc"]
        cur = mysql.connection.cursor()
        cur.execute(f"update todoapitb set todoTitle='{title}',todoDescription='{desc}' where todoid={todoid}")
        cur.connection.commit()
        return redirect("/")
    else:
        cur.execute(f"select * from todoapitb where todoid={todoid}")
        data = cur.fetchone()
        return render_template("todo.html",todo=data)
        
    

if __name__ == "__main__":
    app.run(debug=True)