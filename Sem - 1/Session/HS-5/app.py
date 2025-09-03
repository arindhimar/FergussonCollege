from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route("/")
@app.route("/todos")
def todos():
    cur=mysql.connection.cursor()
    cur.execute('select * from todoapitb')
    data=cur.fetchall()
    return render_template('todo.html',todos=data)

@app.route("/add",methods=["GET","POST"])
def add_todo():
    if request.method=="POST":
        todoTitle=request.form['title']
        todoDescription=request.form['desc']
        cur=mysql.connection.cursor()
        cur.execute(f"insert into todoapitb (todoTitle, todoDescription) values('{todoTitle}','{todoDescription}')")
        mysql.connection.commit()
        return redirect("/")
        
    else:
        return render_template("add_todo.html")

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    cur=mysql.connection.cursor()
    # print(todo_id)
    cur.execute(f"delete from todoapitb where todoid={todo_id}")
    mysql.connection.commit()
    return redirect("/")

@app.route("/edit/<int:todo_id>",methods=["GET","POST"])
def edit_todo(todo_id):
    if request.method=="POST":
        print(request.form)
        todoTitle = request.form["title"]
        todoDescription = request.form["description"]
        
        cur=mysql.connection.cursor()
        cur.execute(f"update todoapitb set todoTitle='{todoTitle}',todoDescription='{todoDescription}' where todoid={todo_id}")
        mysql.connection.commit()
        
        return redirect("/")
    else:
        cur = mysql.connection.cursor()
        cur.execute(f"select * from todoapitb where todoid={todo_id}")
        data=cur.fetchone()
        print(data)
        return render_template("edit.html",todo=data)

if __name__ == "__main__":
    app.run(debug=True)

