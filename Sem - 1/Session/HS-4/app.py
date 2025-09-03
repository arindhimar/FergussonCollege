from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'

mysql = MySQL(app)

@app.route('/todos')
def todos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todoapitb")
    data = cur.fetchall()
    return render_template('todos.html', todos=data)

@app.route('/todos/<int:todo_id>/delete')
def delete_todo(todo_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM todoapitb WHERE todoid = %s", (todo_id,))
    mysql.connection.commit()
    return redirect('/todos')

@app.route('/todos/<int:todo_id>/edit', methods=['GET', 'POST'])
def edit_todo(todo_id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur.execute("UPDATE todoapitb SET todoTitle = %s, todoDescription = %s WHERE todoid = %s", (title, description, todo_id))
        mysql.connection.commit()
        return redirect('/todos')
    cur.execute("SELECT * FROM todoapitb WHERE todoid = %s", (todo_id,))
    todo = cur.fetchone()
    return render_template('edit_todo.html', todo=todo)

@app.route('/todos/new', methods=['GET', 'POST'])
def new_todo():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO todoapitb (todoTitle, todoDescription) VALUES (%s, %s)", (title, description))
        mysql.connection.commit()
        return redirect('/todos')
    return render_template('new_todo.html')

if __name__ == '__main__':
    app.run(debug=True)