from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql=MySQL(app)

@app.route("/")
def home():
    # print("Home Page Accessed")
    exe=mysql.connection.cursor()
    exe.execute("select * from todoapitb")
    data=exe.fetchall()
    print(data)
    return render_template("index.html",tasks=data)

@app.route("/add",methods=["POST"])
def add_task():
    exe=mysql.connection.cursor()
    todotitle=request.form['task']
    
    tododesc=request.form['desc']
    # print(request.form)
    exe.execute(f"insert into todoapitb(todoTitle,todoDescription) values('{todotitle}','{tododesc}')")
    mysql.connection.commit()

    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    exe=mysql.connection.cursor()
    exe.execute(f"delete from todoapitb where todoid={task_id}")
    mysql.connection.commit()
    return redirect("/")

@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update_task(task_id):
    exe=mysql.connection.cursor()
    if request.method == "POST":
        # todotitle=request.form['task']
        # tododesc=request.form['desc']
        # exe.execute(f"update todoapitb set todoTitle='{todotitle}', todoDescription='{tododesc}' where id={task_id}")
        # mysql.connection.commit()
        # return redirect("/")
        pass
    else:
        exe.execute(f"select * from todoapitb where todoid={task_id}")
        task=exe.fetchone()
        return render_template("update.html", task=task)

if __name__=="__main__":
    app.run(debug=True)