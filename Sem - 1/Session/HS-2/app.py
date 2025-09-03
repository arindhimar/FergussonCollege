from flask import Flask, render_template, redirect,request
from flask_mysqldb import MySQL

app = Flask(__name__)  


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todoapidb'


mysql = MySQL(app)

@app.route('/todos')
def show_todos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todoapitb")
    data = cur.fetchall()
    return render_template('todos.html', todos=data)


@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO todoapitb (todoTitle, todoDescription) VALUES (%s, %s)", (title, desc))
        mysql.connection.commit()
        cur.close()

        return redirect('/todos')
    return render_template('add.html')

@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']
        cur.execute("""
            UPDATE todoapitb 
            SET todoTitle=%s, todoDescription=%s 
            WHERE todoId=%s
        """, (title, desc, todo_id))
        mysql.connection.commit()
        cur.close()
        return redirect('/todos')
    cur.execute("SELECT * FROM todoapitb WHERE todoId=%s", (todo_id,))
    todo = cur.fetchone()
    print(todo)
    cur.close()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM todoapitb WHERE todoId=%s", (todo_id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/todos')


if __name__ == "__main__":
    app.run(debug=True)


