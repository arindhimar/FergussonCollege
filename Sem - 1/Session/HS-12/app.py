from flask import Flask,render_template,request,redirect,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route("/")
def get_todos():
    #make it dictionary
    
    con = mysql.connection.cursor()
    
    con.execute("select * from todoapitb")
    todos = con.fetchall()
    #disctionary format
    todos_list = []
    for todo in todos:
        todos_list.append({
            "id": todo[0],
            "title": todo[1],
            "description": todo[2]
        })
        
    # print(todos)
    # return render_template("index.html",todos=todos)
    return jsonify(todos_list),200

@app.route("/delete/<int:todoid>")
def delete_todo(todoid):
    con = mysql.connection.cursor()
    con.execute(f"delete from todoapitb where todoId={todoid}")
    con.connection.commit()
    # return redirect("/")
    return jsonify({"message":"Todo deleted successfully"}),200
        

@app.route("/add",methods=["POST"])
def add_todo():
    # print(request.form['title'])
    #get from josn
    title = request.json['title']
    desc = request.json['desc']
    con = mysql.connection.cursor()
    con.execute(f"insert into todoapitb(todoTitle,todoDescription) values('{title}','{desc}')")
    con.connection.commit()
    
    # return redirect("/")   
    return jsonify({"message":"Todo added successfully"}),201

@app.route("/edit/<int:todoid>",methods=["GET","POST"])
def edit_todo(todoid):
    con = mysql.connection.cursor()
    if request.method =="POST":
        title = request.form['title']
        desc = request.form['desc']
        con.execute(f"update todoapitb set todoTitle = '{title}', todoDescription = '{desc}' where todoId = {todoid}")
        con.connection.commit()
        # return redirect("/")
        return jsonify({"message":"Todo updated successfully"}),200
    else:
        con.execute(f"select * from todoapitb where todoid={todoid}")
        data = con.fetchone()
        print(data)
        # return render_template("index.html",edit_todo=data)
        return jsonify(data),200

if __name__== "__main__":
    app.run(debug=True)