from flask import Flask,render_template,jsonify,request
from mysql import connector
from controllers.teacher_controller import teacher

app = Flask(__name__)

app.register_blueprint(teacher,url_prefix='/teachers')


conn = connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="school_db"
)

cursor = conn.cursor(dictionary=True)

@app.route("/courses")
def get_courses():
    cursor.execute("select * from courses")
    data=cursor.fetchall()
    print(data)
    return jsonify(data),200

@app.route("/teachers")
def get_teachers():
    cursor.execute("select * from teachers")
    data=cursor.fetchall()
    # print(data)
    return jsonify(data),200

@app.route("/teachers",methods=["POST"])
def add_teachers():
    data = request.get_json()
    full_name = data['full_name']
    email = data['email']
    cursor.execute(f"insert into teachers(full_name,email) values('{full_name}','{email}')")
    # cursor.connection.commit()
    return jsonify({"message":"data addedd!!"}),200


@app.route("/teachers/<int:tid>",methods=["DELETE"])
def delete_teachers(tid):
    cursor.execute(f"delete from teachers where teacher_id={tid}")
    # cursor.connection.commit()
    return jsonify({"message":"data deleted!!"}),200


@app.route("/teachers/<int:tid>",methods=["PUT"])
def update_teachers(tid):
    data = request.get_json()
    full_name=data['full_name']
    email = data['email']
    cursor.execute(f"update teachers set full_name='{full_name}',email='{email}' where teacher_id={tid}")
    # cursor.connection.commit()
    return jsonify({"message":"data upadted!!"}),200



if __name__ == "__main__":
    app.run(debug=True)